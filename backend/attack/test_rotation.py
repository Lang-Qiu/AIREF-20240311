from pathlib import Path

from torchvision import transforms
from torchvision.datasets import MNIST
from ...backend import settings
from .rotation import generate_rotation_dataset


def test_generate_rotation_dataset():
    default_dataset_dir = settings.BASE_DIR / "data" / "default_dataset"
    rotation_dataset_dir = settings.BASE_DIR / "data" / "rotation_dataset"
    if not Path.exists(rotation_dataset_dir):
        Path.mkdir(rotation_dataset_dir)
    dataset = MNIST(default_dataset_dir, download=True, transform=transforms.ToTensor())
    degrees = 30
    x_, y_, filename = generate_rotation_dataset(rotation_dataset_dir, dataset, degrees)
    transform = transforms.Compose(
        [
            transforms.RandomRotation(degrees),
        ]
    )
    images = transform(dataset.data)
    images = images.unsqueeze(1).numpy()
    labels = dataset.targets.numpy()
    assert (x_.shape == images.shape) and (y_.shape == labels.shape)
