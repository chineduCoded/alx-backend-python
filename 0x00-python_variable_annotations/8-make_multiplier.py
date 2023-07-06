#!/usr/bin/env python3
"""
8-make_multiplier.py
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a callable function"""
    def multiply(value: float) -> float:
        return value * multiplier
    return multiply
