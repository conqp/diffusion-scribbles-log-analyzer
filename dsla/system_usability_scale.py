"""System usability scale questionnaire."""

from __future__ import annotations
from typing import NamedTuple


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
    score: float

    @classmethod
    def from_csvs(
            cls,
            questionnaire: list[str],
            scores: list[str],
            score: float
    ) -> SystemUsabilityScale:
        """Create SUS data from a CSV record."""
        return cls(
            SUSAttributes.from_csv(questionnaire),
            SUSAttributes.from_csv(scores),
            score
        )
