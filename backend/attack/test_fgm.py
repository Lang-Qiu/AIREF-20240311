from pathlib import Path

import numpy as np
from art.attacks.evasion import FastGradientMethod
from torchvision import transforms
from torchvision.datasets import MNIST
from ..models.model import Net
from ...backend import settings
from .classifier import get_classifier
from .fgm import generate_fgm_dataset


def test_generate_fgm_dataset():
    default_dataset_dir = settings.BASE_DIR / "data" / "default_dataset"
    fgm_dataset_dir = settings.BASE_DIR / "data" / "fgm_dataset"
    if not Path.exists(fgm_dataset_dir):
        Path.mkdir(fgm_dataset_dir)
    model = Net()
    test = False
    dataset = MNIST(default_dataset_dir, download=True, transform=transforms.ToTensor())
    x_, y_, filename = generate_fgm_dataset(fgm_dataset_dir, dataset, model, test)

    x_array = []
    y_array = []
    for x, y in dataset:
        x = x.cpu().numpy()
        x_array.append(x)
        y_array.append(y)
        if test == True:
            break
    x_array = np.array(x_array)
    y_array = np.array(y_array)
    classifier = get_classifier(model)
    fgm = FastGradientMethod(estimator=classifier, eps=0.15)
    x_attack = fgm.generate(x_array)
    x_attack = (x_attack * 255.0).astype(np.uint8)
    assert (x_ == x_attack).all() and (y_ == y_array).all()
