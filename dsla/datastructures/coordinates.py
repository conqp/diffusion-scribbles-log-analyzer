"""2D Coordinates."""

from __future__ import annotations
from typing import NamedTuple


__all__ = ['Coordinates']


class Coordinates(NamedTuple):
    """2D coordinates of a scatter plot."""

    x: int
    y: int

    @classmethod
    def from_strings(cls, x: str, y: str) -> Coordinates:
        """Create coordinates from strings."""
        return cls(int(x), int(y))
