#!/usr/bin/env python3
"""
This is a simple module and it only has
one function called async_generator
"""

from typing import Generator
import random
import asyncio

async def async_generator() -> int:
    """loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10

    Yields:
        Generator[int, None, None]: random number
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
