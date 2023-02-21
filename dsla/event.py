"""Task event."""

from __future__ import annotations
from dataclasses import dataclass
from datetime import time
from typing import Any, Iterable

from dsla.color_change_action import ColorChangeAction
from dsla.coordinates import Coordinates
from dsla.dataset import Dataset
from dsla.rgb import RGB
from dsla.selection_method import SelectionMethod


__all__ = ['Event']


@dataclass
class Event:
    """Type of event."""

    timestamp: time
    type: str

    @classmethod
    def from_csv(cls, record: Iterable[str]) -> Event:
        """Create an event from the respective CSV record."""
        timestamp, typ, *additional_fields = record
        return (clas := EVENTS[typ])(
            time.fromisoformat(timestamp),
            typ,
            *clas.parse_additional_fields(*additional_fields)
        )

    @classmethod
    def parse_additional_fields(cls, *args) -> Iterable[Any]:
        """Set additional data fields."""
        return args


@dataclass
class StartAction(Event):
    """A start action."""

    selection_method: SelectionMethod
    dataset: Dataset

    @classmethod
    def parse_additional_fields(
            cls,
            selection_method: str,
            dataset: str
    ) -> tuple[SelectionMethod, Dataset]:
        return (
            SelectionMethod.from_string(selection_method),
            Dataset(dataset)
        )


@dataclass
class TrainingTaskStart(StartAction):
    """A new training task has started."""


@dataclass
class ChangeMethod(Event):
    """Method change."""

    new_method: SelectionMethod

    @classmethod
    def parse_additional_fields(
            cls,
            new_method: str
    ) -> tuple[SelectionMethod]:
        return SelectionMethod.from_string(new_method),


@dataclass
class Reset(Event):
    """Method reset."""


@dataclass
class DatasetLoaded(Event):
    """Dataset has been loaded."""

    dataset: Dataset

    @classmethod
    def parse_additional_fields(cls, dataset: str) -> tuple[Dataset]:
        return Dataset(dataset),


@dataclass
class CoordinateEvent(Event):
    """Event with coordinates."""

    coordinates: Coordinates

    @classmethod
    def parse_additional_fields(cls, x: str, y: str) -> tuple[Coordinates]:
        print('CALLED')
        return Coordinates.from_strings(x, y),


@dataclass
class DrawStart(CoordinateEvent):
    """User started drawing."""


@dataclass
class Draw(CoordinateEvent):
    """User is drawing."""


@dataclass
class DrawStop(CoordinateEvent):
    """User stopped drawing."""


@dataclass
class ColorAction(Event):
    """A color-related action."""

    number: int     # Color number
    color: RGB
    action: ColorChangeAction

    @classmethod
    def parse_additional_fields(
            cls,
            number: str,
            color: str,
            action: str
    ) -> tuple[int, RGB, ColorChangeAction]:
        return (
            int(number),
            RGB.from_string(color),
            ColorChangeAction(action)
        )


@dataclass
class ColorChange(ColorAction):
    """User changed a color."""


@dataclass
class UserSelectionFinished(Event):
    """User has finished the selection."""


@dataclass
class TrainingTaskFinished(Event):
    """User has finished a training task."""


@dataclass
class TaskStart(StartAction):
    """A new study task has started."""


@dataclass
class ColorAdd(ColorAction):
    """User added a custom color."""


@dataclass
class TaskFinished(Event):
    """User has finished a study task."""


EVENTS = {
    'TRAINING-TASK-START': TrainingTaskStart,
    'CHANGE-METHOD': ChangeMethod,
    'RESET': Reset,
    'DATASET-LOADED': DatasetLoaded,
    'DRAW-START': DrawStart,
    'DRAW': Draw,
    'DRAW-STOP': DrawStop,
    'COLOR-CHANGE': ColorChange,
    'USER-SELECTION-FINISHED': UserSelectionFinished,
    'TRAINING-TASK-FINISHED': TrainingTaskFinished,
    'TASK-START': TaskStart,
    'COLOR-ADD': ColorAdd,
    'TASK-FINISHED': TaskFinished
}
