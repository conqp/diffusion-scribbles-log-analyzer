"""System Usability scale plotting."""

from matplotlib import pyplot

from dsla.datastructures import Experiment, SelectionMethod
from dsla.functions import dict_to_kv
from dsla.statistics import average_sus


__all__ = ['plot_selection_method']


def plot_selection_method(experiments: list[Experiment]) -> None:
    """Plot the System Usability Scale of the respective selection method."""

    x, y = dict_to_kv(average_sus(experiments))
    pyplot.bar(x, y)
    pyplot.title('Average System Usability Scale results')
    pyplot.xlabel('Statement')
    pyplot.ylabel('Points (1-5)')
    pyplot.xticks(x)
    pyplot.show()
