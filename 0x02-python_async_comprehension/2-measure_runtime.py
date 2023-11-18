#!/usr/bin/env python3

"""
This is a simple module and it only has
one function called measure_runtime
"""

async_comprehension = __import__('1-async_comprehension').async_comprehension


import time
import asyncio


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel using asyncio.gather

    Returns:
        float: execution time
    """
    start = time.perf_counter()

    comprehensions = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*comprehensions)

    end = time.perf_counter()
    exec_time = end - start
    return exec_time
