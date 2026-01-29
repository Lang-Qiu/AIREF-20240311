from pathlib import Path

import numpy as np
from torchvision import transforms
from torchvision.datasets import MNIST
from .salt_and_pepper_noise import generate_salt_and_pepper_noise_dataset
from .salt_and_pepper_noise import add_salt_and_pepper_noise
from ...backend import settings


def test_generate_gauss_noise_dataset():
    default_dataset_dir = settings.BASE_DIR / "data" / "default_dataset"
    sp_noise_dataset_dir = settings.BASE_DIR / "data" / "salt_and_pepper_noise_dataset"
    if not Path.exists(sp_noise_dataset_dir):
        Path.mkdir(sp_noise_dataset_dir)
    dataset = MNIST(default_dataset_dir, download=True, transform=transforms.ToTensor())
    noise_level = 0.2
    x_, y_, filename = generate_salt_and_pepper_noise_dataset(
        sp_noise_dataset_dir, dataset, noise_level
    )
    images = dataset.data.numpy()
    labels = dataset.targets.numpy()
    noise_images = np.zeros_like(images)
    for i in range(len(images)):
        noise_images[i] = add_salt_and_pepper_noise(images[i], noise_level)
    noise_images = np.expand_dims(noise_images, 1)
    assert (x_.shape == noise_images.shape) and (y_.shape == labels.shape)
