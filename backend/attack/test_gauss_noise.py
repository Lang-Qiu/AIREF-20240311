from pathlib import Path

import numpy as np
from torchvision import transforms
from torchvision.datasets import MNIST
from ...backend import settings
from .gauss_noise import generate_gauss_noise_dataset


def test_generate_gauss_noise_dataset():
    default_dataset_dir = settings.BASE_DIR / "data" / "default_dataset"
    gauss_noise_dataset_dir = settings.BASE_DIR / "data" / "gauss_noise_dataset"
    if not Path.exists(gauss_noise_dataset_dir):
        Path.mkdir(gauss_noise_dataset_dir)
    dataset = MNIST(default_dataset_dir, download=True, transform=transforms.ToTensor())
    noise_level = 100
    x_, y_, filename = generate_gauss_noise_dataset(
        gauss_noise_dataset_dir, dataset, noise_level
    )
    images = dataset.data.unsqueeze(1).numpy()
    labels = dataset.targets.numpy()
    noise = np.random.normal(scale=noise_level, size=images.shape)
    noise_images = np.clip(images + noise, 0, 255).astype(np.uint8)
    assert (x_.shape == noise_images.shape) and (y_.shape == labels.shape)
