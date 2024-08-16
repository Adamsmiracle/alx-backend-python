#!/usr/bin/env python3

from typing import Union, Tuple

"""Basic annotations for for variables
"""


def to_kv(k: str, v: Union[str, float]) -> tuple[str, float]:
    """_summary_

    Returns:
        tuple[str, float]
    """

    tup = (k, float(v**2))
    return tup
