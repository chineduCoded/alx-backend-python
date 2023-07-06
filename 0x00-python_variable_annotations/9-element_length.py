#!/usr/bin/env python3
"""
9-element_length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Computes the length of a list"""
    return [(i, len(i)) for i in lst]
