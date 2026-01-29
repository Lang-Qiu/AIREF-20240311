import os

import numpy as np
from torchvision import transforms

filename = "crop"


def generate_crop_dataset(save_path, dataset, size):
    transform = transforms.Compose(
        [
            transforms.RandomCrop(size),
            transforms.Resize((28, 28)),
        ]
    )
    images = transform(dataset.data)
    images = images.unsqueeze(1).numpy()
    labels = dataset.targets.numpy()
    filepath = os.path.join(save_path, filename)
    np.savez_compressed(filepath, x=images, y=labels)
    return images, labels, filename
