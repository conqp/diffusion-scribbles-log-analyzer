"""Demographics related graphs."""

from matplotlib import pyplot

from dsla.datastructures import ParticipantData
from dsla.statistics import age_distribution, self_assessment_distribution

__all__ = ['plot_age_distribution', 'plot_self_assessment_distribution']


def plot_age_distribution(experiments: list[ParticipantData]) -> None:
    """Plot the age distribution."""

    age_dist = age_distribution(experiments)
    pyplot.bar(age_dist.keys(), age_dist.values())
    pyplot.title("Participants' age distribution")
    pyplot.xlabel('Age (years)')
    pyplot.ylabel('Amount of participants')
    pyplot.xticks(list(age_dist.keys()))
    pyplot.show()


def plot_self_assessment_distribution(
        experiments: list[ParticipantData]
) -> None:
    """Plot the self-assessment distribution."""

    for index, (key, values) in enumerate(
            self_assessment_distribution(experiments).items(),
            start=-1
    ):
        pyplot.bar(
            [x + index * 0.2 for x in values.keys()],
            values.values(),
            0.2,
            label=key
        )

    pyplot.title("Participants' self-assessment")
    pyplot.ylabel('Amount of participants')
    pyplot.legend()
    pyplot.show()
