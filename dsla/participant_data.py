"""Per-participant study data."""

from typing import NamedTuple

from dsla.participant import Participant
from dsla.study import Study
from dsla.task import Task


class ParticipantData(NamedTuple):
    """Per-participant study data."""

    study: Study
    participant: Participant
    tasks: list[Task]
