#!/usr/bin/env python3
"""
From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay), and returns
total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time.
"""

import asyncio

import time
from typing import List
from asyncio import run


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay)
    Args:
    n - integer rep number of times to spawn wait_random
    max_delay - integer - max delay between each call
    Returns: total_time / n.
    """
    start_time = time.perf_counter()
    run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time
    average_time = total_time / n

    return average_time
