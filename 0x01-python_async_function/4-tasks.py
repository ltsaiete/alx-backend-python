#!/usr/bin/env python3
"""
This is a simple module and it only has
one function called task_wait_random
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay.

    Args:
        n (int): times to execute wait_random
        max_delay (int): max delay

    Returns:
        List[float]: list of all the delays
    """

    tasks = [task_wait_random(max_delay) for i in range(n)]
    delays = [await delay for delay in asyncio.as_completed(tasks)]
    return delays
