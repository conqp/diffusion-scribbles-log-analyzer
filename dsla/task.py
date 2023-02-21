"""Selection task."""

from typing import NamedTuple

from dsla.event import Event
from dsla.selection_method import SelectionMethod


__all__ = ['Task']


class Task(NamedTuple):
    """Selection task of one specific method."""

    selection_method: SelectionMethod
    training_tasks: list[Event]
    study_tasks: list[StudyTask]
    tlx_weighs: TLXWeighs
