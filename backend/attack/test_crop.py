from pathlib import Path

from torchvision import transforms
from torchvision.datasets import MNIST

from ...backend import settings
from .crop import generate_crop_dataset


def test_generate_crop_dataset():
    default_dataset_dir = settings.BASE_DIR / "data" / "default_dataset"
    crop_dataset_dir = settings.BASE_DIR / "data" / "crop_dataset"
    if not Path.exists(crop_dataset_dir):
        Path.mkdir(crop_dataset_dir)
    dataset = MNIST(default_dataset_dir, download=True, transform=transforms.ToTensor())
    size = (20, 20)
    x_, y_, filename = generate_crop_dataset(crop_dataset_dir, dataset, size)
    transform = transforms.Compose(
        [
            transforms.RandomCrop(size),
            transforms.Resize((28, 28)),
        ]
    )
    images = transform(dataset.data)
    images = images.unsqueeze(1).numpy()
    labels = dataset.targets.numpy()
    assert (x_.shape == images.shape) and (y_.shape == labels.shape)
