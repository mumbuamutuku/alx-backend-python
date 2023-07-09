#!/usr/bin/env python3
"""
a type-annotated function to_kv that takes a string k and an int OR float v as arguments
returns a tuple. The first element of the tuple is the string k
The second element is the square of the int/float v and should be annotated as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts an int or float value to a tuple with the string key and the square of the value.
    Args: k: A string rep of key
    v: an int / float value
    Returns: Tuple - string ke and square of v
    """
    return (k, float(v) ** 2)
