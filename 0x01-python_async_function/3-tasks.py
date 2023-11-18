#!/usr/bin/env python3
"""
This is a simple module and it only has
one function called task_wait_random
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """that takes an integer max_delay and returns a asyncio.Task

    Args:
        max_delay (int): max delay

    Returns:
        asyncio.Task: asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
