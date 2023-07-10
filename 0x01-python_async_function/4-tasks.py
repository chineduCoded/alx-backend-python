#!/usr/bin/env python3
"""
4-tasks.py
"""
import asyncio
from typing import List
from asyncio import Task
from random import seed

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
    delays = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        await task
        delay = task.result()
        delays.append(delay)

    return delays


if __name__ == "__main__":
    seed(1)  # Set the random seed for reproducibility
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
