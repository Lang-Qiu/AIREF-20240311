import os
import torch
from .model_io import export_torch_model_to_onnx
from .model_io import export_to_torchscript, load_model_by_torchscript
from .model_io import load_model_by_struct
from pathlib import Path
from backend.backend import settings

from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision import transforms

from ..models.model import Net


source_model_path = settings.BASE_DIR.parent / "resources" / "tests" / "model.pth"
file_path = settings.BASE_DIR.parent / "resources" / "tests" / "net-test.onnx"


def test_export_torch_model_to_onnx():
    # load a torch model
    net = Net()
    checkpoint = torch.load(source_model_path)
    net.load_state_dict(checkpoint["model_state_dict"])
    print(net)
    # export to onnx
    dummy_input = torch.randn(1, 1, 28, 28)
    if os.path.exists(file_path):
        os.remove(file_path)
    export_torch_model_to_onnx(net, dummy_input, file_path)
    assert os.path.exists(file_path)
    # os.remove(file_path)


def test_export_to_torchscript():
    model = Net()
    path_and_filename = settings.BASE_DIR.parent / "resources" / "tests" / "model.pt"
    export_to_torchscript(model, path_and_filename)
    assert Path(path_and_filename).exists()


def test_load_model_by_struct():
    path_and_filename = settings.BASE_DIR.parent / "resources" / "tests" / "model.pth"
    model = load_model_by_struct(Net, path_and_filename)
    default_dataset_dir = settings.BASE_DIR / "data" / "default_dataset"
    dataset = MNIST(default_dataset_dir, download=True, transform=transforms.ToTensor())
    dataloader = DataLoader(dataset=dataset, batch_size=4)
    for x, y in dataloader:
        logits = model(x)
        break


# def test_load_model_by_torchscript():
#     path_and_filename = settings.BASE_DIR.parent / "resources" / "tests" / "model.pt"
#     model = load_model_by_torchscript(path_and_filename)
#     # 读取数据集
#     default_dataset_dir = settings.BASE_DIR / "data" / "default_dataset"
#     dataset = MNIST(default_dataset_dir, download=True, transform=transforms.ToTensor())
#     for x, y in dataset:
#         logits = model(x)
#         break
