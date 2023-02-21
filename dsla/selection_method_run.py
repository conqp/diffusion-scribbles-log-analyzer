"""Selection method run."""

from typing import NamedTuple

from dsla.nasa_tlx import NASA_TLX
from dsla.selection_method import SelectionMethod
from dsla.study_task import StudyTask
from dsla.system_usability_scale import SystemUsabilityScale
from dsla.training_task import TrainingTask


__all__ = ['SelectionMethodRun']


class SelectionMethodRun(NamedTuple):
    """Selection method run."""

    selection_method: SelectionMethod
    training: list[TrainingTask]
    tasks: list[StudyTask]
    system_usability_scale: SystemUsabilityScale
    nasa_tlx: NASA_TLX
