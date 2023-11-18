#!/usr/bin/env python3
"""
This is a simple module and it only has
one function called async_comprehension
"""

from typing import List
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random numbers using an
    async comprehensing over async_generator

    Returns:
        List[float]: random numbers
    """

    gen = async_generator()
    numbers = [n async for n in gen]
    return numbers
