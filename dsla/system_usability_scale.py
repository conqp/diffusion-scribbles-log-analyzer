"""System usability scale questionnaire."""

from typing import NamedTuple


__all__ = ['SystemUsabilityScale']


class SystemUsabilityScale(NamedTuple):
    """System usability scale questionnaire."""

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
