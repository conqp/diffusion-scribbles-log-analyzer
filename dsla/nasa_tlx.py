"""NASA TLX questionnaire."""

from typing import NamedTuple


__all__ = ['NASA_TLX']


class NASA_TLX(NamedTuple):
    """NASA TLX questionnaire."""

    mental_demand: int
    physical_demand: int
    temporal_demand: int
    performance: int
    effort: int
    frustration: int
    score: float
