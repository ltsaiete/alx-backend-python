#!/usr/bin/env python3

"""
This is a simple module and it only has
one function called wait_n
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay.

    Args:
        n (int): times to execute wait_random
        max_delay (int): max delay

    Returns:
        List[float]: list of all the delays
    """

    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    delays = [await delay for delay in asyncio.as_completed(tasks)]
    return delays
