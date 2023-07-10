#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    measures the total execution time for wait_n(n, max_delay)
    Args:
    n - integer rep number of times to spawn wait_random
    max_delay - integer - max delay between each call
    Returns: total_time / n.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await t for t in asyncio.as_completed(tasks)]
