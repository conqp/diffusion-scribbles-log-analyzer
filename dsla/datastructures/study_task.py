"""A study task with additional data."""

from functools import cache
from typing import Any, NamedTuple

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
    def precisions(self) -> list[tuple[int, Precision]]:
        """Returns the precisions for each class of this task."""
        return cached_precisions(self)

    @property
    def correct_pct(self) -> float:
        """Percentage of correct classifications."""
        return sum(self.correct) / len(self.correct) * 100

    def to_json(self) -> dict[str, Any]:
        """Return a JSON-ish dict."""
        return {
            'events': self.events.to_json(),
            'summary': self.summary.to_json(),
            'classification': self.classification,
            'correct': self.correct,
            'correct_pct': self.correct_pct
        }


@cache
def cached_precisions(study_task: StudyTask) -> list[tuple[int, Precision]]:
    """Returns the precisions for each class of this task."""

    return list(
        Precision.from_classification(
            study_task.classification,
            study_task.dataset.solution
        )
    )
