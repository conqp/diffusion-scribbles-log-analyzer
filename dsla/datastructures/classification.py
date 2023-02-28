"""Classification list."""


__all__ = ['Classification', 'CorrectClassifications']


class Classification(tuple[int | None]):
    """Classification data."""


class CorrectClassifications(tuple[bool]):
    """Correct classifications."""
