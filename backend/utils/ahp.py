import torch


def ahp_score_cal(eval_index, weight_static, weight_dynamic, weight_criterion):
    # 需要根据具体指标进行修改
    static_index = torch.tensor(eval_index[:2]).reshape(1, -1)
    dynamic_index = torch.tensor(eval_index[2:]).reshape(1, -1)

    static_score = torch.matmul(static_index, weight_static.reshape(-1, 1))
    dynamic_score = torch.matmul(dynamic_index, weight_dynamic.reshape(-1, 1))
    concat_score = torch.cat([static_score, dynamic_score], dim=0)
    final_score = torch.matmul(
        concat_score.reshape(1, -1), weight_criterion.reshape(-1, 1)
    )

    return final_score
