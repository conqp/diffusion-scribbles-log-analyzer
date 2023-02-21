"""Selection method run."""

from typing import NamedTuple

from dsla.event import Event
from dsla.nasa_tlx import NASA_TLX
from dsla.selection_method import SelectionMethod
from dsla.study_task import StudyTask
from dsla.system_usability_scale import SystemUsabilityScale


__all__ = ['SelectionMethodRun']


class SelectionMethodRun(NamedTuple):
    """Selection method run."""

    selection_method: SelectionMethod
    training: list[Event]
    tasks: list[StudyTask]
    system_usability_scale: SystemUsabilityScale
    nasa_tlx: NASA_TLX
