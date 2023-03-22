"""Selection task summary."""

from __future__ import annotations
from datetime import timedelta
from re import findall
from typing import Any, NamedTuple

from dsla.datastructures.dataset import Dataset
from dsla.datastructures.rgb import RGB
from dsla.datastructures.selection_method import SelectionMethod


__all__ = ['Summary']


CLASSES_REGEX = r'\(\d+, \d+, \d+\)'


class Summary(NamedTuple):
    """Selection task summary."""

    method: SelectionMethod
    dataset: Dataset
    task_duration: timedelta
    draw_duration: timedelta
    invert_count: int
    undo_count: int
    redo_count: int
    reset_count: int
    scribble_count: int
    scribble_pixels: int
    eraser_count: int
    classes: tuple[RGB]

    @classmethod
    def from_csv(cls, record: list[str]) -> Summary:
        """Create a Summary from a CSV record."""
        (
            method, dataset, task_duration, draw_duration, invert_count,
            undo_count, redo_count, reset_count, scribble_count,
            scribble_pixels, eraser_count, classes
        ) = record
        return cls(
            SelectionMethod.from_string(method),
            Dataset(dataset),
            timedelta(seconds=float(task_duration)),
            timedelta(seconds=float(draw_duration)),
            int(invert_count),
            int(undo_count),
            int(redo_count),
            int(reset_count),
            int(scribble_count),
            int(scribble_pixels),
            int(eraser_count),
            tuple(parse_classes(classes))
        )

    def to_json(self) -> dict[str, Any]:
        """Return a JSON-ish dict."""
        return {
            'method': self.method,
            'dataset': self.dataset,
            'task_duration': self.task_duration.total_seconds(),
            'draw_duration': self.draw_duration.total_seconds(),
            'invert_count': self.invert_count,
            'undo_count': self.undo_count,
            'redo_count': self.redo_count,
            'reset_count': self.reset_count,
            'scribble_count': self.scribble_count,
            'scribble_pixels': self.scribble_pixels,
            'eraser_count': self.eraser_count,
            'classes': self.classes
        }


def parse_classes(text: str) -> list[RGB]:
    """Parse classes."""

    for cls in findall(CLASSES_REGEX, text):
        yield RGB.from_string(cls)
