#!/usr/bin/env python3
"""
4-tasks.py
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn multiple tasks of task_wait_random asynchronously and return the list of delays.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay value.

    Returns:
        List[float]: The list of delays.
    """
    delay_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(delay_times)
