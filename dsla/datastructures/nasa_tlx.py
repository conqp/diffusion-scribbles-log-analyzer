"""NASA TLX questionnaire."""

from __future__ import annotations
from typing import NamedTuple


__all__ = ['NASA_TLX', 'TLXAttributes']


class TLXAttributes(NamedTuple):
    """NASA TLX attributes."""

    mental_demand: int
    physical_demand: int
    temporal_demand: int
    overall_performance: int
    effort: int
    frustration_level: int

    @classmethod
    def from_csv(cls, record: list[str]) -> TLXAttributes:
        """Create NASA TLX attributes from a CSV record."""
        (
            mental_demand, physical_demand, temporal_demand,
            overall_performance, effort, frustration_level
        ) = record
        return cls(
            int(mental_demand),
            int(physical_demand),
            int(temporal_demand),
            int(overall_performance),
            int(effort),
            int(frustration_level)
        )


class NASA_TLX(NamedTuple):
    """NASA TLX questionnaire."""

    raw: TLXAttributes
    weighted: TLXAttributes
    score: float

    @classmethod
    def from_csvs(
            cls,
            raw: list[str],
            weighted: list[str],
            score: float
    ) -> NASA_TLX:
        """Create a NASA TLX record from a CSV record."""
        return cls(
            TLXAttributes.from_csv(raw),
            TLXAttributes.from_csv(weighted),
            score
        )
