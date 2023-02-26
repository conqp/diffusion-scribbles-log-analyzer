"""Demographics statistics."""

from statistics import mean, stdev
from typing import Any

from dsla.datastructures import Participant, ParticipantData


__all__ = ['average_demographics']


def average_demographics(
        experiments: list[ParticipantData]
) -> dict[str, Any]:
    """Return a dict of average demographics."""

    return _average_demographics(
        [experiment.participant for experiment in experiments]
    )


def _average_demographics(participants: list[Participant]) -> dict[str, Any]:
    """Returns a dict of average demographics."""

    return {
        'age': {
            'mean': (
                xbar := mean(participant.age for participant in participants)
            ),
            'stdev': stdev(
                [participant.age for participant in participants],
                xbar=xbar
            )
        }
    }
