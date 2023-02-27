"""Demographics related graphs."""

from matplotlib import pyplot

from dsla.datastructures import Experiment
from dsla.functions import dict_to_kv
from dsla.statistics import age_distribution, self_assessment_distribution

__all__ = ['plot_age_distribution', 'plot_self_assessment_distribution']


def plot_age_distribution(experiments: list[Experiment]) -> None:
    """Plot the age distribution."""

    x, y = dict_to_kv(age_distribution(experiments))
    pyplot.bar(x, y)
    pyplot.title("Participants' age distribution")
    pyplot.xlabel('Age (years)')
    pyplot.ylabel('Amount of participants')
    pyplot.xticks(x)
    pyplot.show()


def plot_self_assessment_distribution(
        experiments: list[Experiment]
) -> None:
    """Plot the self-assessment distribution."""

    for index, (key, values) in enumerate(
            self_assessment_distribution(experiments).items(),
            start=-1
    ):
        x, y = dict_to_kv(values)
        x = [p + index * 0.2 for p in x]
        pyplot.bar(x, y, 0.2, label=key)

    pyplot.title("Participants' self-assessment")
    pyplot.ylabel('Amount of participants')
    pyplot.legend()
    pyplot.show()
