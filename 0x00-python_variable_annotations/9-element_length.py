#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return
values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns a list of tuples
    Args: lst - a list of strings
    """
    return [(i, len(i)) for i in lst]
