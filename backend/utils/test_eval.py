import os

import numpy as np
import torch
from torch.utils.data import DataLoader, TensorDataset

from ..settings import BASE_DIR
from .eval import eval, eval_on_all

model_path = BASE_DIR.parent / "resources" / "tests" / "model.pt"
dataset_dir = BASE_DIR.parent / "resources" / "tests"
filenames = [
    "fgm",
    "pgd",
    "cw",
    "df",
    "pa",
    "gauss_noise",
    "salt_and_pepper_noise",
    "crop",
    "rotation",
    "blur",
]


def test_eval():
    acc_ = eval(dataset_dir, filename="fgm", model_path=model_path)
    data = np.load(os.path.join(dataset_dir, "fgm.npz"))
    x_test = torch.from_numpy(data["x"]).float()
    y_test = torch.from_numpy(data["y"]).float()
    dataset = TensorDataset(x_test, y_test)
    dataloader = DataLoader(dataset=dataset, batch_size=256, shuffle=True)

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = torch.jit.load(model_path, map_location=device)
    model.eval()

    total = 0
    correct = 0
    for inputs, labels in dataloader:
        inputs, labels = inputs.to(device), labels.to(device)
        outputs = model(inputs)
        pred = torch.argmax(outputs.data, dim=1)
        total += labels.size(0)
        correct += (pred == labels).sum().item()
    acc = correct * 100 / total
    print("acc: %.2f%%" % acc)
    assert acc == acc_


def test_eval_on_all():
    acc_list_test = eval_on_all(dataset_dir, filenames, model_path)
    acc_list = []
    for filename in filenames:
        acc = eval(dataset_dir, filename, model_path)
        acc_list.append(acc)
    assert acc_list_test == acc_list
