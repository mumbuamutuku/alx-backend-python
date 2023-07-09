#!/usr/bin/env python3
"""
a type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates Sum of a lst
    Args: mxd_list: A list of int and floats
    Returns: Sum of the list
    """
    res = 0.0
    for n in mxd_lst:
        res += n
    return res
