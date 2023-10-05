#!/usr/bin/env python3
"""
This is a simple module and it only has
one function called to_kv
"""
from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """takes a string k and an int OR float v as arguments and returns a tuple.

    Args:
        k (str): _description_
        v (int | float): _description_

    Returns:
        Tuple[str, float]: _description_
    """
    v_square = v ** 2
    return (k, v_square)
