import os

import numpy as np
import torch
from torch.utils.data import DataLoader, TensorDataset


def eval_on_benign(dataset, model_path):
    dataloader = DataLoader(dataset=dataset, batch_size=256, shuffle=True)
    total = 0
    correct = 0
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = torch.jit.load(model_path, map_location=device)
    model.eval()
    for inputs, labels in dataloader:
        inputs, labels = inputs.to(device), labels.to(device)
        outputs = model(inputs)
        pred = torch.argmax(outputs.data, dim=1)
        total += labels.size(0)
        correct += (pred == labels).sum().item()
    acc = correct * 100 / total
    print(acc)
    return acc


def eval(save_path, filename, model_path):
    data = np.load(os.path.join(save_path, filename + ".npz"))
    x_test = torch.from_numpy(data["x"]).float()
    y_test = torch.from_numpy(data["y"]).float()
    dataset = TensorDataset(x_test, y_test)
    dataloader = DataLoader(dataset=dataset, batch_size=256, shuffle=True)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = torch.jit.load(model_path, map_location=device)
    model.eval()

    total = 0
    correct = 0
    for inputs, labels in dataloader:
        inputs, labels = inputs.to(device), labels.to(device)
        outputs = model(inputs)
        pred = torch.argmax(outputs.data, dim=1)
        total += labels.size(0)
        correct += (pred == labels).sum().item()
    acc = correct * 100 / total
    print(acc)
    return acc


def eval_on_all(save_path, filenames, model_path):
    acc_list = []
    for filename in filenames:
        acc = eval(save_path, filename, model_path)
        acc_list.append(acc)
    print(acc_list)
    return acc_list
