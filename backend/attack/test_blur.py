from pathlib import Path

from torchvision import transforms
from torchvision.datasets import MNIST
from ...backend import settings
from .blur import generate_blur_dataset


def test_generate_blur_dataset():
    default_dataset_dir = settings.BASE_DIR / "data" / "default_dataset"
    blur_dataset_dir = settings.BASE_DIR / "data" / "blur_dataset"
    if not Path.exists(blur_dataset_dir):
        Path.mkdir(blur_dataset_dir)
    dataset = MNIST(default_dataset_dir, download=True, transform=transforms.ToTensor())
    sigma = (0.1, 2.0)
    x_, y_, filename = generate_blur_dataset(blur_dataset_dir, dataset, sigma)
    transform = transforms.Compose(
        [transforms.GaussianBlur(kernel_size=21, sigma=sigma)]
    )
    images = transform(dataset.data)
    images = images.unsqueeze(1).numpy()
    labels = dataset.targets.numpy()
    assert (x_.shape == images.shape) and (y_.shape == labels.shape)
