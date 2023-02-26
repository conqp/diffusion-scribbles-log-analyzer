"""A study task with additional data."""

from typing import NamedTuple

from dsla.datastructures.classification import Classification, CorrectClassifications
from dsla.datastructures.dataset import Dataset
from dsla.datastructures.summary import Summary
from dsla.datastructures.task import Task


__all__ = ['StudyTask']


class StudyTask(NamedTuple):
    """Study task information."""

    events: Task
    summary: Summary
    classification: Classification
    correct: CorrectClassifications

    @property
    def dataset(self) -> Dataset:
        """Return the dataset."""
        return self.events.dataset
