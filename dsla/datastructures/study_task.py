"""A study task with additional data."""

from typing import NamedTuple

from dsla.datastructures.classification import Classification
from dsla.datastructures.classification import CorrectClassifications
from dsla.datastructures.dataset import Dataset
from dsla.datastructures.precision import Precision
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

    @property
    def precisions(self) -> dict[int, Precision]:
        """Returns the precisions for each class of this task."""
        return dict(
            Precision.from_classification(
                self.classification,
                self.dataset.solution
            )
        )
