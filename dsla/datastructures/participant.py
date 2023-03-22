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

    @property
    def vision_ok(self) -> bool:
        """ Returns True if the participant has no corrected vision or
        normal vision.
        """
        return not self.corrected_vision or self.normal_vision

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

    def to_json(self) -> dict[str, bool | int | str]:
        """Return a JSON-ish dict."""
        return {
            'age': self.age,
            'gender': self.gender,
            'corrected_vision': self.corrected_vision,
            'normal_vision': self.normal_vision,
            'computer_experience': self.computer_experience,
            'data_visualization_experience':
                self.data_visualization_experience,
            'scatter_plot_experience': self.scatter_plot_experience,
            'vision_ok': self.vision_ok
        }
