"""User weights for the NASA TLX questionnaire."""

from typing import NamedTuple


__all__ = ['TLXWeights']


class TLXWeights(NamedTuple):
    """NASA TLS questionnaire weights."""

    mental_demand: int
    physical_demand: int
    temporal_demand: int
    overall_performance: int
    effort: int
    frustration_level: int
