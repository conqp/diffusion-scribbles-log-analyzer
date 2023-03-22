"""Task event."""

from __future__ import annotations
from dataclasses import dataclass
from datetime import time
from typing import Any, Iterable

from dsla.datastructures.color_change_action import ColorChangeAction
from dsla.datastructures.coordinates import Coordinates
from dsla.datastructures.dataset import Dataset
from dsla.datastructures.rgb import RGB
from dsla.datastructures.selection_method import SelectionMethod


__all__ = ['Event', 'TrainingTaskStart', 'TaskStart']


@dataclass(frozen=True)
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

    def to_json(self) -> dict[str, Any]:
        """Return a JSON-ish dict."""
        return {
            'timestamp': self.timestamp.isoformat(),
            'type': self.type
        }


@dataclass(frozen=True)
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

    def to_json(self) -> dict[str, Any]:
        """Return a JSON-ish dict."""
        return {
            **super.to_json(),
            'selection_method': self.selection_method,
            'dataset': self.dataset
        }


@dataclass(frozen=True)
class TrainingTaskStart(StartAction):
    """A new training task has started."""


@dataclass(frozen=True)
class ChangeMethod(Event):
    """Method change."""

    new_method: SelectionMethod

    @classmethod
    def parse_additional_fields(
            cls,
            new_method: str
    ) -> tuple[SelectionMethod]:
        return SelectionMethod.from_string(new_method),

    def to_json(self) -> dict[str, Any]:
        """Return a JSON-ish dict."""
        return {
            **super.to_json(),
            'new_method': self.new_method
        }


@dataclass(frozen=True)
class Reset(Event):
    """Method reset."""


@dataclass(frozen=True)
class DatasetLoaded(Event):
    """Dataset has been loaded."""

    dataset: Dataset

    @classmethod
    def parse_additional_fields(cls, dataset: str) -> tuple[Dataset]:
        return Dataset(dataset),

    def to_json(self) -> dict[str, Any]:
        """Return a JSON-ish dict."""
        return {
            **super.to_json(),
            'dataset': self.dataset
        }


@dataclass(frozen=True)
class CoordinateEvent(Event):
    """Event with coordinates."""

    coordinates: Coordinates

    @classmethod
    def parse_additional_fields(cls, x: str, y: str) -> tuple[Coordinates]:
        return Coordinates.from_strings(x, y),

    def to_json(self) -> dict[str, Any]:
        """Return a JSON-ish dict."""
        return {
            **super.to_json(),
            'coordinates': self.coordinates
        }


@dataclass(frozen=True)
class DrawStart(CoordinateEvent):
    """User started drawing."""


@dataclass(frozen=True)
class Draw(CoordinateEvent):
    """User is drawing."""


@dataclass(frozen=True)
class DrawStop(CoordinateEvent):
    """User stopped drawing."""


@dataclass(frozen=True)
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

    def to_json(self) -> dict[str, Any]:
        """Return a JSON-ish dict."""
        return {
            **super.to_json(),
            'number': self.number,
            'color': self.color,
            'action': self.action
        }


@dataclass(frozen=True)
class ColorChange(ColorAction):
    """User changed a color."""


@dataclass(frozen=True)
class UserSelectionFinished(Event):
    """User has finished the selection."""


@dataclass(frozen=True)
class TrainingTaskFinished(Event):
    """User has finished a training task."""


@dataclass(frozen=True)
class TaskStart(StartAction):
    """A new study task has started."""


@dataclass(frozen=True)
class ColorAdd(ColorAction):
    """User added a custom color."""


@dataclass(frozen=True)
class Invert(Event):
    """Color inversion event."""


@dataclass(frozen=True)
class ChangeBrushSize(Event):
    """User changed brush size."""

    from_: int
    to: int

    @classmethod
    def parse_additional_fields(
            cls,
            from_: str,
            _: str,
            to: str
    ) -> Iterable[Any]:
        return int(from_), int(to)

    def to_json(self) -> dict[str, Any]:
        """Return a JSON-ish dict."""
        return {
            **super.to_json(),
            'from': self.from_,
            'to': self.to
        }


@dataclass(frozen=True)
class EraseStart(CoordinateEvent):
    """User started to erase."""


@dataclass(frozen=True)
class Erase(CoordinateEvent):
    """User is erasing."""


@dataclass(frozen=True)
class EraseStop(CoordinateEvent):
    """User stopped erasing."""


@dataclass(frozen=True)
class Undo(Event):
    """User undid last action."""


@dataclass(frozen=True)
class Redo(Event):
    """User redid last undone action."""


@dataclass(frozen=True)
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
    'INVERT': Invert,
    'CHANGE-BRUSH-SIZE': ChangeBrushSize,
    'ERASE-START': EraseStart,
    'ERASE': Erase,
    'ERASE-STOP': EraseStop,
    'UNDO': Undo,
    'REDO': Redo,
    'TASK-FINISHED': TaskFinished
}
