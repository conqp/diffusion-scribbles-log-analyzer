"""RGB color."""

from __future__ import annotations
from typing import NamedTuple


__all__ = ['RGB']


class RGB(NamedTuple):
    """Red-green-blue color."""

    red: int
    green: int
    blue: int

    @classmethod
    def from_string(cls, text: str) -> RGB:
        """Create an RGB color from a string tuple."""
        red, green, blue = map(
            str.strip, text.lstrip('(').rstrip(')').split(',')
        )
        return cls(int(red), int(green), int(blue))
