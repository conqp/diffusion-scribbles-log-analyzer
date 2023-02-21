"""Per-participant study data."""

from typing import NamedTuple

from dsla.participant import Participant
from dsla.selection_method_run import SelectionMethodRun
from dsla.study import Study


__all__ = ['ParticipantData']


class ParticipantData(NamedTuple):
    """Per-participant study data."""

    study: Study
    participant: Participant
    runs: list[SelectionMethodRun]
