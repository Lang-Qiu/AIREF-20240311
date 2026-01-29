from pathlib import Path

import numpy as np
from art.attacks.evasion import CarliniL0Method
from torchvision import transforms
from torchvision.datasets import MNIST

from ...backend import settings
from ..models.model import Net
from .classifier import get_classifier
from .cw import generate_cw_dataset


def test_generate_cw_dataset():
    default_dataset_dir = settings.BASE_DIR / "data" / "default_dataset"
    cw_dataset_dir = settings.BASE_DIR / "data" / "cw_dataset"
    if not Path.exists(cw_dataset_dir):
        Path.mkdir(cw_dataset_dir)
    model = Net()
    dataset = MNIST(default_dataset_dir, download=True, transform=transforms.ToTensor())
    x_, y_, filename = generate_cw_dataset(cw_dataset_dir, dataset, model, test=False)

    x_array = []
    y_array = []
    for x, y in dataset:
        x = x.cpu().numpy()
        x_array.append(x)
        y_array.append(y)
        break
    x_array = np.array(x_array)
    y_array = np.array(y_array)
    classifier = get_classifier(model)
    cw = CarliniL0Method(classifier=classifier)
    x_attack = cw.generate(x_array)
    x_attack = (x_attack * 255.0).astype(np.uint8)
    assert (x_ == x_attack).any() and (y_ == y_array).any()
