#!/usr/bin/env python3
"""
7-to_kv.py
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a turple"""
    return k, float(v**2)
