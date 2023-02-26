"""Selection method run."""

from __future__ import annotations
from typing import Any, Iterator, NamedTuple

from dsla.datastructures.event import TrainingTaskStart, TaskStart
from dsla.datastructures.nasa_tlx import NASA_TLX
from dsla.datastructures.selection_method import SelectionMethod
from dsla.datastructures.study_task import StudyTask
from dsla.datastructures.summary import Summary
from dsla.datastructures.classification import Classification, CorrectClassifications
from dsla.datastructures.system_usability_scale import SystemUsabilityScale
from dsla.datastructures.task import Task
from dsla.datastructures.training_task import TrainingTask

__all__ = ['SelectionMethodRun']


class SelectionMethodRun(NamedTuple):
    """Selection method run."""

    selection_method: SelectionMethod
    training: list[TrainingTask]
    tasks: list[StudyTask]
    system_usability_scale: SystemUsabilityScale
    nasa_tlx: NASA_TLX

    @classmethod
    def from_items(
            cls,
            items: list[Any],
            selection_method: SelectionMethod
    ) -> SelectionMethodRun:
        """Create a selection method run from the given items."""
        return cls(
            selection_method,
            list(filter_training_tasks(items)),
            list(filter_study_tasks(items)),
            get_sus(items),
            get_nasa_tlx(items)
        )


def filter_training_tasks(items: list[Any]) -> Iterator[TrainingTask]:
    """Filter the training tasks."""

    for item in items:
        if isinstance(item, Task) and isinstance(item[0], TrainingTaskStart):
            yield TrainingTask(item)


def filter_study_tasks(items: list[Any]) -> Iterator[StudyTask]:
    """Filter the study tasks."""

    events = summary = classification = correct = None

    for item in items:
        if isinstance(item, Task) and isinstance(item[0], TaskStart):
            events = item

        if events is not None:
            if summary is None and isinstance(item, Summary):
                summary = item

            if classification is None and isinstance(item, Classification):
                classification = item

            if correct is None and isinstance(item, CorrectClassifications):
                correct = item

        if all(
                item is not None for item in [
                    events, summary, classification, correct
                ]
        ):
            yield StudyTask(events, summary, classification, correct)
            events = summary = classification = correct = None


def get_sus(items: list[Any]) -> SystemUsabilityScale:
    """Returns the system usability scale."""

    if (amount := len(
            sus := [
                item for item in items
                if isinstance(item, SystemUsabilityScale)
            ]
    )) != 1:
        raise ValueError(f'Expected exactly one SUS but got {amount}')

    return sus[0]


def get_nasa_tlx(items: list[Any]) -> NASA_TLX:
    """Returns the NSA TLX."""

    if (amount := len(
            nsa_tlx := [
                item for item in items
                if isinstance(item, NASA_TLX)
            ]
    )) != 1:
        raise ValueError(f'Expected exactly one NASA TLX but got {amount}')

    return nsa_tlx[0]
