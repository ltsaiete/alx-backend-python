#!/usr/bin/env python3
"""
This is a simple module and it only has
one function called sum_mixed_list
"""
from typing import List


def sum_mixed_list (mxd_lst : List[int | float] ) -> float:
    """takes a list mxd_lst  of floats as argument and
    returns their sum as a float.

    Args:
        mxd_lst  (List[float]): _description_

    Returns:
        float: _description_
    """
    return sum(mxd_lst )
