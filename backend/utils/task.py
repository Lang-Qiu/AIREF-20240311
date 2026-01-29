import torch
from torchvision import transforms
from torchvision.datasets import MNIST

from attack.cw import generate_cw_dataset
from attack.deepfool import generate_deepfool_dataset
from attack.fgm import generate_fgm_dataset
from attack.pgd import generate_pgd_dataset
from attack.pixel_attack import generate_pa_dataset
from django.conf import settings
from .eval import eval, eval_on_benign


def task_wrapper(task_dict):
    # try:
    # TODO
    print("preparing task")
    if task_dict["task_type"] == "adv_black":
        task = AdvBlackEvalTask(
            attack_list=task_dict["attack_list"],
            record=task_dict["record"],
            dataset=task_dict["dataset"],
            model=task_dict["model"],
        )
        results = task.eval()
    elif task_dict["task_type"] == "adv_white":
        task = Task(
            attack_list=task_dict["attack_list"],
            record=task_dict["record"],
            dataset=task_dict["dataset"],
            model=task_dict["model"],
        )
        print("task created.")
        results = task.eval()
    elif task_dict["task_type"] == "backdoor_model_generate":
        raise NotImplementedError(
            "the type you request: %s not implemented." % task_dict["task_type"]
        )
    else:
        raise NotImplementedError(
            "the type you request: %s not implemented." % task_dict["task_type"]
        )
    print("results:", results)
    print("eval finished.")

    # generate pdf report here

    # except Exception as e:
    #     print("task execute failed.")
    #     exc_type, exc_value, exc_traceback = sys.exc_info()
    #     traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=open("./error_file_test.log", 'w+'))


class Task(object):
    def __init__(
        self, test_type, attack_list, record, dataset: str = None, model: str = None
    ) -> None:
        self.dataset_name = dataset
        self.model_name = model
        self.attack_list = attack_list
        self.record = record

    def eval(self):
        """
        评估部分的入口，不接受任何参数
        """
        results = {"benign": None, "FGM": None}
        # 加载数据集与模型
        default_set = self.get_dataset()
        model = self.get_model()
        # 生成测试数据并获取测试结果
        save_path = settings.BASE_DIR / "UserData" / self.record["username"] / "dataset"
        model_path = (
            settings.BASE_DIR / "UserData" / self.record["username"] / "model" / self.record["modelname"]
        )
        for attack_type in self.attack_list:
            match attack_type:
                case "benign":
                    result = eval_on_benign(default_set, model_path)
                    results["benign"] = result
                case "FGM":
                    _, _, filename = generate_fgm_dataset(save_path, default_set, model)
                    result = eval(save_path, filename, model_path)
                    results["FGM"] = result
                case "CW":
                    _, _, filename = generate_cw_dataset(save_path, default_set, model)
                    result = eval(save_path, filename, model_path)
                    results["CW"] = result
                case "DEEPFOOL":
                    _, _, filename = generate_deepfool_dataset(
                        save_path, default_set, model
                    )
                    result = eval(save_path, filename, model_path)
                    results["DEEPFOOL"] = result
                case "PGD":
                    _, _, filename = generate_pgd_dataset(save_path, default_set, model)
                    result = eval(save_path, filename, model_path)
                    results["PGD"] = result
                case "PIXEL":
                    _, _, filename = generate_pa_dataset(save_path, default_set, model)
                    result = eval(save_path, filename, model_path)
                    results["PIXEL"] = result
                case "other_attack":
                    pass
                case _:
                    raise ValueError("no matched attack implemented.")
        return results

    def get_dataset(self):
        match self.dataset_name.lower():
            case "mnist":
                dataset = MNIST(
                    self.default_dataset_dir,
                    download=True,
                    transform=transforms.ToTensor(),
                )
                return dataset
            case "cifar10":
                pass
            case "imagenet":
                pass
            case _:
                raise ValueError("dataset not found.")

    @property
    def model_path(self):
        model_dir = self.user_dir / "model"
        model_name = "model.pt"
        path_and_filename_to_model = model_dir / model_name

        return path_and_filename_to_model

    def get_model(self):
        from models.model import Net

        model = Net()
        return model

    @property
    def user_dir(self):
        return settings.BASE_DIR / "UserData" / self.record["username"]

    @property
    def default_dataset_dir(self):
        return settings.BASE_DIR / "data" / "default_dataset"


class AdvBlackEvalTask:
    def eval():
        pass
