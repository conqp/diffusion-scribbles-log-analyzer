"""Participant demographic data."""

from __future__ import annotations
from configparser import ConfigParser
from typing import NamedTuple

from dsla.datastructures.gender import Gender


__all__ = ['Participant']


class Participant(NamedTuple):
    """Participant demographic data."""

    age: int
    gender: Gender
    corrected_vision: bool  # Glasses required?
    normal_vision: bool     # Glasses worn?
    computer_experience: int
    data_visualization_experience: int
    scatter_plot_experience: int

    @classmethod
    def from_csv(cls, record: list[str]) -> Participant:
        """Create a new Participant from a CSV record."""
        (
            age, gender, corrected_vision, normal_vision, computer_experience,
            data_visualization_experience, scatter_plot_experience
        ) = record
        return cls(
            int(age),
            Gender.from_string(gender),
            ConfigParser.BOOLEAN_STATES[corrected_vision.lower()],
            ConfigParser.BOOLEAN_STATES[normal_vision.lower()],
            int(computer_experience),
            int(data_visualization_experience),
            int(scatter_plot_experience)
        )
