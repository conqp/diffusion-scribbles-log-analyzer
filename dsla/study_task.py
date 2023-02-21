"""A study task with additional data."""

from typing import NamedTuple

from dsla.classification import Classification, CorrectClassifications
from dsla.event import Event
from dsla.summary import Summary


__all__ = ['StudyTask']


class StudyTask(NamedTuple):
    """Study task information."""

    events: list[Event]
    summary: Summary
    classification: Classification
    correct: CorrectClassifications
