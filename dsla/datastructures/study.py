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

    def to_json(self) -> dict[str, str]:
        """Return a JSON-ish dict."""
        return {
            'timestamp': self.timestamp.isoformat(),
            'participant_id': self.participant_id
        }
