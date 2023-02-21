"""A task."""

from dsla.event import Event


__all__ = ['Task']


class Task(list[Event]):
    """A list of events."""
