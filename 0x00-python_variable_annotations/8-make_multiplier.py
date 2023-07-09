#!/usr/bin/env python3
"""
a type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies
a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a func that multiplies a float b the given multiplier
    Args: Multiplier: a float multiplier vakue
    Returns: A function
    """
    def multi_func(n: float) -> float:
        """ Inner function to perfotm multiplication
        Args: n - a float value
        Return: the product of n and multiplier
        """
        return n * multiplier
    return multi_func
