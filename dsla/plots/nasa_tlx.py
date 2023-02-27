"""Plotting of the NASA-TLX questionnaires."""

from matplotlib import pyplot

from dsla.datastructures import Experiment, SelectionMethod
from dsla.statistics import average_tlx


__all__ = ['plot_nasa_tlx']


STATEMENTS_SHORT = [
    'mental demand',
    'physical demand',
    'temporal demand',
    'performance',
    'effort',
    'frustration'
]


def plot_nasa_tlx(experiments: list[Experiment], offset: float = -0.3) -> None:
    """Plots the raw and weighted NASA-TLX distributions."""

    _plot_nasa_tlx(experiments, 'raw', offset=offset)
    _plot_nasa_tlx(experiments, 'weighted', offset=offset)


def _plot_nasa_tlx(
        experiments: list[Experiment],
        key: str,
        offset: float = -0.3
) -> None:
    """Plot the weighted NASA-TLX averages."""

    for index, (method, nasa_tlx) in enumerate(
            average_tlx(experiments)['methods'].items()
    ):
        y = list(nasa_tlx[key].values())
        x = range(len(y))
        pyplot.bar(
            [p + offset + index * 0.2 for p in x],
            y,
            0.2,
            label=SelectionMethod(method).canonical_name
        )

    pyplot.xticks(
        range(len(STATEMENTS_SHORT)),
        STATEMENTS_SHORT,
        rotation=-45,
        ha='left'
    )
    pyplot.subplots_adjust(bottom=0.25)
    pyplot.title(f'Average {key} NASA-TLX results')
    pyplot.ylabel('Score')
    pyplot.legend(loc='upper left')
    pyplot.show()
