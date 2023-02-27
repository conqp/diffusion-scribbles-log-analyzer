"""System Usability scale plotting."""

from matplotlib import pyplot

from dsla.datastructures import Experiment, SelectionMethod
from dsla.statistics import average_sus


__all__ = ['plot_sus']


def plot_sus(experiments: list[Experiment], offset=-0.3) -> None:
    """Plot the System Usability Scale of the respective selection method."""

    for index, (method, avg_sus) in enumerate(
            average_sus(experiments).items()
    ):
        y = list(avg_sus['questionnaire'].values())
        x = range(1, len(y) + 1)
        pyplot.bar(
            [p + offset + index * 0.2 for p in x],
            y,
            0.2,
            label=SelectionMethod(method).value.capitalize()
        )

    pyplot.xticks(x)
    pyplot.title('Average System Usability Scale results')
    pyplot.xlabel('Statement no.')
    pyplot.ylabel('Points (1-5)')
    pyplot.legend(loc='center')
    pyplot.show()
