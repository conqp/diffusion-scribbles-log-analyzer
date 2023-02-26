"""Demographics statistics."""

from statistics import mean, stdev
from typing import Any

from dsla.datastructures import Gender, Participant, ParticipantData

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
            ),
            'min': min(participant.age for participant in participants),
            'max': max(participant.age for participant in participants)
        },
        'genders': {
            'male': sum(
                participant.gender is Gender.MALE for participant in
                participants
            ) / len(participants),
            'female': sum(
                participant.gender is Gender.FEMALE for participant in
                participants
            ) / len(participants),
            'n/a': sum(
                participant.gender is Gender.NO_ANSWER for participant in
                participants
            ) / len(participants)
        },
        'corrected_vision': sum(
            participant.corrected_vision for participant in participants
        ) / len(participants),
        'normal_vision': sum(
            participant.normal_vision for participant in participants
        ) / len(participants),
        'vision_ok': sum(
            participant.vision_ok for participant in participants
        ) / len(participants),
        'computer_experience': {
            'mean': (
                xbar := mean(
                    participant.computer_experience for participant
                    in participants
                )
            ),
            'stdev': stdev(
                [
                    participant.computer_experience for participant
                    in participants
                ],
                xbar=xbar
            )
        },
        'data_visualization_experience': {
            'mean': (
                xbar := mean(
                    participant.data_visualization_experience for participant
                    in participants
                )
            ),
            'stdev': stdev(
                [
                    participant.data_visualization_experience for participant
                    in participants
                ],
                xbar=xbar
            )
        },
        'scatter_plot_experience': {
            'mean': (
                xbar := mean(
                    participant.scatter_plot_experience for participant
                    in participants
                )
            ),
            'stdev': stdev(
                [
                    participant.scatter_plot_experience for participant
                    in participants
                ],
                xbar=xbar
            )
        }
    }
