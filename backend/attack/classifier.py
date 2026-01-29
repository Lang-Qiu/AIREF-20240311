import torch
from art.estimators.classification import PyTorchClassifier


def get_classifier(model):
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    classifier = PyTorchClassifier(
        model=model,
        clip_values=(0.0, 255.0),
        loss=criterion,
        optimizer=optimizer,
        input_shape=(1, 28, 28),
        nb_classes=10,
    )
    return classifier
