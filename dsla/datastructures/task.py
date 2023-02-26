"""A task."""

from dsla.datastructures.dataset import Dataset
from dsla.datastructures.event import Event, TrainingTaskStart, TaskStart


__all__ = ['Task']


class Task(list[Event]):
    """A list of events."""

    @property
    def dataset(self) -> Dataset:
        """Return the dataset."""
        for event in self:
            if isinstance(event, (TrainingTaskStart, TaskStart)):
                return event.dataset

        raise ValueError('No dataset information available.')
