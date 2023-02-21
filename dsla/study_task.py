"""A study task with additional data."""

from typing import NamedTuple

from dsla.event import Event
from dsla.summary import Summary


__all__ = ['StudyTask']


class StudyTask(NamedTuple):
    """Study task information."""

    events: list[Event]
    summary: Summary
    classification: list[int]
    correct: list[int]
