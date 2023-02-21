"""A study task with additional data."""

from typing import NamedTuple

from dsla.classification import Classification, CorrectClassifications
from dsla.dataset import Dataset
from dsla.event import Event, TrainingTaskStart, TaskStart
from dsla.summary import Summary


__all__ = ['StudyTask']


class StudyTask(NamedTuple):
    """Study task information."""

    events: list[Event]
    summary: Summary
    classification: Classification
    correct: CorrectClassifications

    @property
    def dataset(self) -> Dataset:
        """Return the dataset."""
        for event in self.events:
            if isinstance(event, (TrainingTaskStart, TaskStart)):
                return event.dataset

        raise ValueError('No dataset information available.')
