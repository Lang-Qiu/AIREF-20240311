import os

import numpy as np
from torchvision import transforms

filename = "blur"


def generate_blur_dataset(save_path, dataset, sigma):
    transform = transforms.Compose(
        [transforms.GaussianBlur(kernel_size=21, sigma=sigma)]
    )
    images = transform(dataset.data)
    images = images.unsqueeze(1).numpy()
    labels = dataset.targets.numpy()
    filepath = os.path.join(save_path, filename)
    np.savez_compressed(filepath, x=images, y=labels)
    return images, labels, filename
