# --------------------------------------------------------
# BiCSL
# Written by Yuwei Sun https://github.com/yuweisunn
# Adapted from https://github.com/cuiyuhao1996
# --------------------------------------------------------

import torch


# Masking the sequence mask
def make_mask(feature):
    return (torch.sum(
        torch.abs(feature),
        dim=-1
    ) == 0).unsqueeze(1).unsqueeze(2)