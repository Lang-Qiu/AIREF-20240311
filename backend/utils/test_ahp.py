import torch
from .ahp import ahp_score_cal


def test_ahp_score_cal():
    detail_index = [0.99, 0.80, 0.85, 0.90]
    weight_static = torch.tensor([1.0, 2.0])
    weight_dynamic = torch.tensor([2.0, 1.0])
    weight_criterion = torch.tensor([1.0, 1.0])
    res = ahp_score_cal(detail_index, weight_static, weight_dynamic, weight_criterion)
    assert res == 5.19
