"""Study meta data."""

from datetime import datetime
from typing import NamedTuple


__all__ = ['Study']


class Study(NamedTuple):
    """Study meta data."""

    timestamp: datetime
    participant_id: str
