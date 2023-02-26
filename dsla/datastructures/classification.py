"""Classification list."""


__all__ = ['Classification', 'CorrectClassifications']


class Classification(list[int | None]):
    """Classification data."""


class CorrectClassifications(list[bool]):
    """Correct classifications."""
