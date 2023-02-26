"""Demographics related graphs."""

from matplotlib import pyplot

from dsla.datastructures import ParticipantData
from dsla.statistics import age_distribution

__all__ = ['plot_age_distribution']


def plot_age_distribution(experiments: list[ParticipantData]) -> None:
    """Plot the age distribution."""

    age_dist = age_distribution(experiments)
    pyplot.bar(age_dist.keys(), age_dist.values())
    pyplot.title("Participants' age distribution")
    pyplot.xlabel('Age (years)')
    pyplot.ylabel('Amount of participants')
    pyplot.xticks(list(age_dist.keys()))
    pyplot.show()
