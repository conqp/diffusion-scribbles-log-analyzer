"""Demographics statistics."""

from collections import defaultdict
from statistics import mean, stdev
from typing import Any

from dsla.datastructures import Gender, Participant, ParticipantData

__all__ = [
    'average_demographics',
    'age_distribution',
    'self_assessment_distribution'
]


def average_demographics(
        experiments: list[ParticipantData]
) -> dict[str, Any]:
    """Return a dict of average demographics."""

    return _average_demographics(
        [experiment.participant for experiment in experiments]
    )


def age_distribution(experiments: list[ParticipantData]) -> dict[int, int]:
    """Return the age distribution of the participants."""

    ages = defaultdict(int)

    for experiment in experiments:
        ages[experiment.participant.age] += 1

    return ages


def self_assessment_distribution(
        experiments: list[ParticipantData]
) -> dict[str, dict[int, int]]:
    """Returns the self-assessment distribution."""

    return {
        'computer experience': computer_experience_distribution(experiments),
        'data visualization experience':
            data_visualization_experience_distribution(experiments),
        'scatter plot experience': scatter_plot_experience_distribution(
            experiments
        )
    }


def computer_experience_distribution(
        experiments: list[ParticipantData]
) -> dict[int, int]:
    """Returns the computer experience distribution."""

    computer_experience = defaultdict(int)

    for experiment in experiments:
        computer_experience[experiment.participant.computer_experience] += 1

    return computer_experience


def data_visualization_experience_distribution(
        experiments: list[ParticipantData]
) -> dict[int, int]:
    """Returns the data visualization experience distribution."""

    data_visualization_experience = defaultdict(int)

    for experiment in experiments:
        data_visualization_experience[
            experiment.participant.data_visualization_experience
        ] += 1

    return data_visualization_experience


def scatter_plot_experience_distribution(
        experiments: list[ParticipantData]
) -> dict[int, int]:
    """Returns the scatter plot experience distribution."""

    scatter_plot_experience = defaultdict(int)

    for experiment in experiments:
        scatter_plot_experience[
            experiment.participant.scatter_plot_experience
        ] += 1

    return scatter_plot_experience


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
