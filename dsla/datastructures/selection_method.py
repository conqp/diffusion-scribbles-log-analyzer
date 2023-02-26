"""Selection methods."""

from __future__ import annotations
from enum import Enum


__all__ = ['SelectionMethod']


class SelectionMethod(str, Enum):
    """Available selection methods."""

    LASSO = 'lasso'
    BRUSH = 'brush'
    MAHALANOBIS = 'mahalanobis'
    TWO_SIDED = 'two-sided'

    @classmethod
    def from_string(cls, text: str) -> SelectionMethod:
        """Create a SelectionMethod from the given text."""
        try:
            return cls(name := text.split()[0].lower())
        except ValueError:
            return ALIASES[name]


ALIASES = {
    'lasso-selection': SelectionMethod.LASSO,
    'brush-selection': SelectionMethod.BRUSH,
    'mahalanobis-selection': SelectionMethod.MAHALANOBIS,
    'diffusion-scribbles': SelectionMethod.TWO_SIDED
}
