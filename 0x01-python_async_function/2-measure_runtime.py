#!/usr/bin/env python3
"""
From the previous file, import wait_n into 2-measure_runtime.py.

Create a measure_time function with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay), and returns
total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time.
"""

import asyncio

from time import perf_counter
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay)
    Args:
    n - integer rep number of times to spawn wait_random
    max_delay - integer - max delay between each call
    Returns: total_time / n.
    """
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - start_time
    average_time = total_time / n

    return average_time
