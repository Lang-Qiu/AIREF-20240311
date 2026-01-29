import os

import matplotlib.pyplot as plt
import numpy as np


def add_salt_and_pepper_noise(image, noise_level):
    noise_image = np.copy(image)
    h, w = image.shape
    num_noise_pixels = int(noise_level * h * w)
    for i in range(num_noise_pixels // 2):
        x, y = np.random.randint(0, h), np.random.randint(0, w)
        noise_image[x, y] = 0
    for i in range(num_noise_pixels // 2):
        x, y = np.random.randint(0, h), np.random.randint(0, w)
        noise_image[x, y] = 255
    return noise_image


filename = "salt_and_pepper_noise"


def generate_salt_and_pepper_noise_dataset(save_path, dataset, noise_level):
    images = dataset.data.numpy()
    labels = dataset.targets.numpy()
    noise_images = np.zeros_like(images)
    for i in range(len(images)):
        noise_images[i] = add_salt_and_pepper_noise(images[i], noise_level)
    noise_images = np.expand_dims(noise_images, 1)
    filepath = os.path.join(save_path, filename)
    np.savez_compressed(filepath, x=noise_images, y=labels)
    return noise_images, labels, filename
