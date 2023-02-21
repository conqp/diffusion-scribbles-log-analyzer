"""Gender information."""

from __future__ import annotations
from enum import Enum


__all__ = ['Gender']


class Gender(str, Enum):
    """Available gender selection in the study."""

    MALE = 'male'
    FEMALE = 'female'
    NO_ANSWER = 'n/a'

    @classmethod
    def from_string(cls, gender: str) -> Gender:
        """Return a new instance of Gender from a given string."""
        return cls(gender.lower())
