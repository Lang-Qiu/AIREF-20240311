import os

import numpy as np

filename = "gauss_noise"


def generate_gauss_noise_dataset(save_path, dataset, noise_level):
    images = dataset.data.unsqueeze(1).numpy()
    labels = dataset.targets.numpy()
    noise = np.random.normal(scale=noise_level, size=images.shape)
    noise_images = np.clip(images + noise, 0, 255).astype(np.uint8)
    filepath = os.path.join(save_path, filename)
    np.savez_compressed(filepath, x=noise_images, y=labels)
    return noise_images, labels, filename
