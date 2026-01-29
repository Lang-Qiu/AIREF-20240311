from .task import Task
import numpy as np
from .. import settings
import json

import torch
from torchvision.datasets import MNIST
from torchvision import transforms
from torch.utils.data import DataLoader

task_dict = {
    "task_type": "white",
    "dataset_type": "image",
    "dataset": "mnist",
    "model": "net",
    "attack_list": ["benign"],
    "record": {
        "username": "username",
    },
}


def test_task_get_dataset():
    task = Task("white", ["benign"], ["username"], "mnist", "net")
    dataset = task.get_dataset()
    for x, y in dataset:
        assert isinstance(x.cpu().numpy(), np.ndarray)
        break


def test_task_get_model():
    task = Task("white", ["benign"], ["username"], "mnist", "net")
    model = task.get_model()
    default_dataset_dir = settings.BASE_DIR / "data" / "default_dataset"
    dataset = MNIST(default_dataset_dir, download=True, transform=transforms.ToTensor())
    dataloader = DataLoader(dataset=dataset, batch_size=4)
    for x, y in dataloader:
        assert 1 == 1


def test_task_eval():
    task = Task("white", ["benign", "FGM"], ["username"], "mnist", "net")
    results = task.eval()
    test_dir = settings.BASE_DIR.parent / "resources" / "tests"
    with open(test_dir / "test_task_eval.json", "w", encoding="utf-8") as f:
        json.dump(results, f)
    assert results["benign"] is not None
