#!/usr/bin/env python3
"""
This is a simple module and it only has
one function called make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier : float) -> Callable[[float], float] :
    """takes a float multiplier as argument and returns a function that
    multiplies a float by multiplier.

    Args:
        multiplier (float): _description_

    Returns:
        Callable[[float], float]: _description_
    """
    def fun(n: float) -> float:
        """_summary_

        Args:
            n (float): _description_

        Returns:
            float: _description_
        """
        return multiplier * n

    return fun
