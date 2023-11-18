#!/usr/bin/env python3

"""
This is a simple module and it only has
one function called measure_time
"""

import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n

    Args:
        n (int): times to execute wait_random
        max_delay (int): max delay

    Returns:
        float: total_time / n
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = perf_counter()

    total_time = end - start
    return total_time / n
