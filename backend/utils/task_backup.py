import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from torch.utils.data import DataLoader, Dataset
import numpy as np
from art.attacks.evasion import FastGradientMethod
from art.estimators.classification import PyTorchClassifier
import struct
import os
import argparse
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Image  # 报告内容相关类
from reportlab.lib.pagesizes import letter  # 页面的标志尺寸(8.5*inch, 11*inch)
from backend.backend.utils.report import Graphs, add_watermark


def task_wrapper(task_dict):
    # try:
    # TODO
    print("preparing create task")
    task = Task(
        task_type=task_dict["task_type"],
        attack_list=task_dict["attack_list"],
        record=task_dict["record"],
        dataset=task_dict["dataset"],
        model=task_dict["model"],
    )
    print("task created.")
    results = task.eval()
    print("results:", results)
    print("eval finished.")
    # except Exception as e:
    #     print("task execute failed.")
    #     exc_type, exc_value, exc_traceback = sys.exc_info()
    #     traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=open("./error_file_test.log", 'w+'))


class GetDataset(Dataset):
    """
    读取数据、初始化数据
    """

    def __init__(self, folder, train=False, transform=None):
        (images, labels) = self.load_data(folder, train)
        self.images = images
        self.label = labels
        self.transform = transform

    def __getitem__(self, index):
        img, target = self.images[index], int(self.label[index])
        if self.transform is not None:
            img = self.transform(img)
        return img, target

    def __len__(self):
        return len(self.images)

    """
    load_data也是我们自定义的函数，用途：读取数据集中的数据 ( 图片数据+标签label
    """

    def load_data(self, data_folder, train):
        if train:
            image_file = os.path.join(data_folder, "train-images-idx3-ubyte")
            label_file = os.path.join(data_folder, "train-labels-idx1-ubyte")
        else:
            image_file = os.path.join(data_folder, "test-images-idx3-ubyte")
            label_file = os.path.join(data_folder, "test-labels-idx1-ubyte")
        with open(label_file, "rb") as lbpath:  # rb表示的是读取二进制数据
            labels = np.frombuffer(lbpath.read(), np.uint8, offset=8)
        with open(image_file, "rb") as imgpath:
            images = np.frombuffer(imgpath.read(), np.uint8, offset=16).reshape(
                len(labels), 28, 28
            )
        return (images, labels)


class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.model = torch.nn.Sequential(
            # The size of the picture is 28x28
            torch.nn.Conv2d(
                in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1
            ),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2),
            # The size of the picture is 14x14
            torch.nn.Conv2d(
                in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1
            ),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2),
            # The size of the picture is 7x7
            torch.nn.Conv2d(
                in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1
            ),
            torch.nn.ReLU(),
            torch.nn.Flatten(),
            torch.nn.Linear(in_features=7 * 7 * 64, out_features=128),
            torch.nn.ReLU(),
            torch.nn.Linear(in_features=128, out_features=10),
            torch.nn.Softmax(dim=1),
        )

    def forward(self, input):
        output = self.model(input)
        return output


class Task(object):
    def __init__(
        self, task_type, attack_list, record, dataset: str = None, model: str = None
    ) -> None:
        self.task_type = task_type
        self.transform = transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
        )
        self.train_dataset = GetDataset(dataset, train=True, transform=self.transform)
        self.test_dataset = GetDataset(dataset, train=False, transform=self.transform)
        self.train_dataloader = self.get_dataloader(self.train_dataset)
        self.test_dataloader = self.get_dataloader(self.test_dataset)
        self.dataset_path = dataset
        self.model_path = model
        self.record = (
            record["username"],
            record["create_time"],
            record["dataname"],
            record["modelname"],
        )
        self.attack_list = attack_list
        self.classifier = self.get_classifier()
        self.results = {"benign": None, "FGM": None}

    def get_classifier(self):
        net = Net()
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        net.to(device)
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(net.parameters(), lr=0.001)
        checkpoint = torch.load(self.model)
        net.load_state_dict(checkpoint["model_state_dict"])
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
        net.eval()
        classifier = PyTorchClassifier(
            model=net,
            clip_values=(0.0, 255.0),
            loss=criterion,
            optimizer=optimizer,
            input_shape=(1, 28, 28),
            nb_classes=10,
        )
        return classifier

    def get_dataloader(self, dataset):
        # get all data loader(benign and malicious) @Jiafei_Niu
        print("loading data loader.")
        dataloader = DataLoader(dataset, batch_size=256, shuffle=True)
        return dataloader

    def generate_data(self, attack_type):
        advImg_path = "../backend/UserData/%s/dataset/adv" % self.record[0]
        if not os.path.exists(advImg_path):
            os.mkdir(advImg_path)
        Image = open(advImg_path + "/test-images-idx3-ubyte", "wb")
        Label = open(advImg_path + "/test-labels-idx1-ubyte", "wb")
        Image.write(struct.pack(">4i", 2051, len(self.test_dataset), 28, 28))
        Label.write(struct.pack(">2i", 2049, len(self.test_dataset)))
        for inputs, labels in self.test_dataloader:
            inputs = inputs.numpy()
            labels = labels.numpy()
            attack = FastGradientMethod(estimator=self.classifier, eps=0.15)

            inputs_adv = attack.generate(x=inputs)
            inputs_adv = inputs_adv * 255.0
            inputs_adv = inputs_adv.astype(np.uint8)

            labels = labels.astype(np.uint8)
            adv_image = inputs_adv.tobytes()
            adv_label = labels.tobytes()
            Image.write(adv_image)
            Label.write(adv_label)
        Image.close()
        Label.close()

    def load_model(self, model_path):
        if model_path is None:
            model_path = r"default_model_path"
        print("loading model.")
        # model = ModelForTest(num_class=10)
        return model_path

    def eval(self):
        print("eval process started.")
        self.model = self.load_model(self.model_path)
        # for path in self.dataset_path:
        self.results["benign"] = self.evaluate_on_specific_data(
            self.dataset_path, self.model_path
        )
        self.results["FGM"] = self.evaluate_on_specific_data(
            self.dataset_path + "/adv", self.model_path, self.model_path
        )

        # TODO: 封装成一个函数
        # example：  ret = generate_pdf(self.results)
        content = list()
        # 添加标题
        content.append(Graphs.draw_title("模型评估报告"))

        content.append(Graphs.draw_title(""))
        content.append(Graphs.draw_little_title("模型信息"))
        # 添加表格
        data = [
            (
                "任务创建人",
                "任务创建时间",
                "数据集名称",
                "模型名称",
            ),
            self.record,
        ]
        content.append(Graphs.draw_table(*data))

        content.append(Graphs.draw_title(""))
        content.append(Graphs.draw_little_title("评估结果"))
        # 添加表格
        data = [("攻击方法", "数量", "测试集准确率"), self.results["benign"]]
        content.append(Graphs.draw_table(*data))
        content.append(Graphs.draw_title(""))
        content.append(Graphs.draw_little_title(" "))
        # 添加表格
        data = [
            ("攻击方法", "数量", "测试集准确率"),
            self.results["FGM"],
        ]
        content.append(Graphs.draw_table(*data))
        content.append(Graphs.draw_title(""))
        content.append(Graphs.draw_little_title("评估结果总结"))
        content.append(Graphs.draw_little_text("评估结果汇总"))
        content.append(Graphs.draw_text("您的模型在" + str(self.results["FGM"]) + "中达标"))
        content.append(Graphs.draw_little_text("鲁棒性提升意见"))
        content.append(Graphs.draw_text("无"))
        content.append(
            Graphs.draw_little_text(
                "详细防御提升方案可参考: https://www.yuque.com/docs/share/476e345a-a807-49f8-b490-e1b399ebea75"
            )
        )
        content.append(Graphs.draw_little_text("评级标准"))
        content.append(Graphs.draw_text("低:原始测试集准确率<85% or 标准参数下2个以上的评测项不达标"))
        content.append(Graphs.draw_text("中:原始测试集准确率>=85% and 标准参数下1-2个评测项不达标"))
        content.append(Graphs.draw_text("高:原始测试集准确率>=85% and 标准参数下所有评测项达标"))
        doc = SimpleDocTemplate(
            "../backend/UserData/%s/report.pdf" % self.record[0], pagesize=letter
        )
        doc.build(content)
        add_watermark(
            "../watermark.pdf",
            "../backend/backend/UserData/%s/report.pdf" % self.record[0],
        )
        print("the report has been generated.")
        return self.results

    def evaluate_on_specific_data(self, data_path, model_path, attack_type="benign"):
        cur_data_path = data_path + attack_type
        self.generate_data()
        dataset = GetDataset(cur_data_path, train=False, transform=self.transform)
        dataloader = torch.utils.data.DataLoader(dataset, batch_size=256, shuffle=False)
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        net = Net()
        net.to(device)
        checkpoint = torch.load(model_path)
        net.load_state_dict(checkpoint["model_state_dict"])
        net.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for inputs, labels in dataloader:
                inputs, labels = inputs.to(device), labels.to(device)
                outputs = net(inputs)
                pre = torch.argmax(outputs.data, dim=1)
                total += labels.size(0)
                correct += (pre == labels).sum().item()
            acc = correct * 100 / total
            print("Accuracy: {:.3f}%".format(acc))

        test_results = (attack_type, len(dataset), str(acc) + "%")
        return test_results
