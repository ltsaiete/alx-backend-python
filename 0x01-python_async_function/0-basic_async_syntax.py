#!/usr/bin/env python3
"""
This is a simple module and it only has
one function called fun_name
"""

import time
import random


async def wait_random(max_delay: float) -> float:
    """ waits for a random delay between 0 and max_delay

    Args:
        max_delay (float): the max delay

    Returns:
        float: the delay
    """
    delay = random.random() * max_delay
    time.sleep(delay)
    return delay
