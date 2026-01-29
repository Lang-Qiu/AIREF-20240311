from pathlib import Path

import numpy as np
from art.attacks.evasion import ProjectedGradientDescent
from torchvision import transforms
from torchvision.datasets import MNIST

from ...backend import settings
from ..models.model import Net
from .classifier import get_classifier
from .pgd import generate_pgd_dataset


def test_generate_pgd_dataset():
    default_dataset_dir = settings.BASE_DIR / "data" / "default_dataset"
    pgd_dataset_dir = settings.BASE_DIR / "data" / "pgd_dataset"
    if not Path.exists(pgd_dataset_dir):
        Path.mkdir(pgd_dataset_dir)
    model = Net()
    dataset = MNIST(default_dataset_dir, download=True, transform=transforms.ToTensor())
    x_, y_, filename = generate_pgd_dataset(pgd_dataset_dir, dataset, model, test=False)

    x_array = []
    y_array = []
    for x, y in dataset:
        x = x.cpu().numpy()
        x_array.append(x)
        y_array.append(y)
        # break
    x_array = np.array(x_array)
    y_array = np.array(y_array)
    classifier = get_classifier(model)
    pgd = ProjectedGradientDescent(estimator=classifier, eps=0.15)
    x_attack = pgd.generate(x_array)
    x_attack = (x_attack * 255.0).astype(np.uint8)
    assert (x_ == x_attack).all() and (y_ == y_array).all()
