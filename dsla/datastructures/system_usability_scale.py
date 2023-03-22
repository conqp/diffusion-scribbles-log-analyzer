"""System usability scale questionnaire."""

from __future__ import annotations
from typing import Any, NamedTuple


__all__ = ['SystemUsabilityScale', 'SUSAttributes']


class SUSAttributes(NamedTuple):
    """Attributes of the System Usability Scale questionnaire."""

    use_frequently: int
    too_complex: int
    easy_to_use: int
    tech_support_required: int
    well_integrated: int
    too_inconsistent: int
    easy_to_learn: int
    cumbersome: int
    confident: int
    much_learning_required: int

    @classmethod
    def from_csv(cls, record: list[str]) -> SUSAttributes:
        """Create SUS data from a CSV record."""
        (
            use_frequently, too_complex, easy_to_use, tech_support_required,
            well_integrated, too_inconsistent, easy_to_learn, cumbersome,
            confident, much_learning_required
        ) = record
        return cls(
            int(use_frequently),
            int(too_complex),
            int(easy_to_use),
            int(tech_support_required),
            int(well_integrated),
            int(too_inconsistent),
            int(easy_to_learn),
            int(cumbersome),
            int(confident),
            int(much_learning_required)
        )


class SystemUsabilityScale(NamedTuple):
    """System usability scale questionnaire."""

    questionnaire: SUSAttributes
    scores: SUSAttributes
    pre_calculated_score: float

    @classmethod
    def from_csvs(
            cls,
            questionnaire: list[str],
            scores: list[str],
            pre_calculated_score: float
    ) -> SystemUsabilityScale:
        """Create SUS data from a CSV record."""
        return cls(
            SUSAttributes.from_csv(questionnaire),
            SUSAttributes.from_csv(scores),
            pre_calculated_score
        )

    @property
    def score(self) -> float:
        """Re-calculated score."""
        return sum(
            (5 - attribute) if index % 2 else (attribute - 1)
            for index, attribute in enumerate(self.questionnaire)
        ) * 2.5

    def to_json(self) -> dict[str, Any]:
        """Return a JSON-ish dict."""
        return {
            'questionnaire': self.questionnaire._asdict(),
            'scores': self.scores._asdict(),
            'pre_calculated_score': self.pre_calculated_score
        }
