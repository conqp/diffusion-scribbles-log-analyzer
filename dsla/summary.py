"""Selection task summary."""

from datetime import timedelta
from typing import NamedTuple

from dsla.dataset import Dataset
from dsla.rgb import RGB
from dsla.selection_method import SelectionMethod


__all__ = ['Summary']


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
    classes: list[RGB]
