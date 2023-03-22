"""NASA TLX questionnaire."""

from __future__ import annotations
from typing import Any, NamedTuple


__all__ = ['NASA_TLX', 'TLXAttributes']


SCALING_FACTOR: int = 5


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

    def to_json(self) -> dict[str, int]:
        """Return a JSON-ish dict."""
        return self._asdict()


class NASA_TLX(NamedTuple):
    """NASA TLX questionnaire."""

    raw: TLXAttributes
    weighted: TLXAttributes
    score: float

    @property
    def normalized(self) -> TLXAttributes:
        """Return normalized TLX attributes."""
        return TLXAttributes(*(value * SCALING_FACTOR for value in self.raw))

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

    def calculate_score(self, weightings: TLXAttributes) -> float:
        """Return the re-calculated score."""
        return sum(
            value * weighting * 5
            for value, weighting in zip(self.raw, weightings)
        ) / 15

    def to_json(self) -> dict[str, Any]:
        """Return a JSON-ish dict."""
        return {
            'raw': self.raw.to_json(),
            'weighted': self.weighted.to_json(),
            'score': self.score
        }
