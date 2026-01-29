import os

import numpy as np
from torchvision import transforms

filename = "rotation"


def generate_rotation_dataset(save_path, dataset, degrees):
    transform = transforms.Compose(
        [
            transforms.RandomRotation(degrees),
        ]
    )
    images = transform(dataset.data)
    images = images.unsqueeze(1).numpy()
    labels = dataset.targets.numpy()
    filepath = os.path.join(save_path, filename)
    np.savez_compressed(filepath, x=images, y=labels)
    return images, labels, filename
