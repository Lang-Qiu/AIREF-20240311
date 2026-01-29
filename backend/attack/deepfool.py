import os

import numpy as np
from art.attacks.evasion import DeepFool

from .classifier import get_classifier

filename = "deepfool"


def generate_deepfool_dataset(save_path, dataset, model, test=False):
    x_array = []
    y_array = []
    for x, y in dataset:
        x = x.cpu().numpy()
        x_array.append(x)
        y_array.append(y)
        if test == True:
            break
    x_array = np.array(x_array)
    y_array = np.array(y_array)
    classifier = get_classifier(model)
    df = DeepFool(classifier=classifier, epsilon=0.15)
    x_attack = df.generate(x_array)
    x_attack = (x_attack * 255.0).astype(np.uint8)
    filepath = os.path.join(save_path, filename)
    np.savez_compressed(filepath, x=x_attack, y=y_array)
    return x_attack, y_array, filename
