#!/usr/bin/env python3
"""
2-measure_runtime.py
"""
import time
from typing import List
import asyncio
import random

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and return the average time per iteration.

    Args:
        n (int): The number of iterations.
        max_delay (int): The maximum delay value.

    Returns:
        float: The average time per iteration.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n

if __name__ == "__main__":
    random.seed(1)  # Set the random seed for reproducibility
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
