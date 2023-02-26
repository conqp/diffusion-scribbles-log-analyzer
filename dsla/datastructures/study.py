"""Study meta data."""

from __future__ import annotations
from datetime import datetime
from typing import NamedTuple


__all__ = ['Study']


class Study(NamedTuple):
    """Study meta data."""

    timestamp: datetime
    participant_id: str

    @classmethod
    def from_csv(cls, record: list[str]) -> Study:
        """Create a Study instance from a csv record."""
        timestamp, participant_id = record
        return cls(
            datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S'),
            participant_id
        )
