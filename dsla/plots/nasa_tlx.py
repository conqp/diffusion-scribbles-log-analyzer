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

    plot_raw_nasa_tlx(experiments, offset=offset)
    plot_weighted_nasa_tlx(experiments, offset=offset)


def plot_raw_nasa_tlx(
        experiments: list[Experiment],
        offset: float = -0.3
) -> None:
    """Plot the raw NASA-TLX averages."""

    for index, (method, nasa_tlx) in enumerate(
            average_tlx(experiments)['methods'].items()
    ):
        y = list(nasa_tlx['normalized'].values())
        x = range(1, len(y) + 1)
        pyplot.bar(
            [p + offset + index * 0.2 for p in x],
            y,
            0.2,
            label=SelectionMethod(method).canonical_name
        )

    pyplot.xticks(
        x,
        [
            f'{index} ({short_desc})'
            for index, short_desc in enumerate(STATEMENTS_SHORT, start=1)
        ]
    )
    pyplot.title('Average raw NASA-TLX results')
    pyplot.ylabel('Score')
    pyplot.legend(loc='center')
    pyplot.show()


def plot_weighted_nasa_tlx(
        experiments: list[Experiment],
        offset: float = -0.3
) -> None:
    """Plot the weighted NASA-TLX averages."""

    for index, (method, nasa_tlx) in enumerate(
            average_tlx(experiments)['methods'].items()
    ):
        y = list(nasa_tlx['weighted'].values())
        x = range(1, len(y) + 1)
        pyplot.bar(
            [p + offset + index * 0.2 for p in x],
            y,
            0.2,
            label=SelectionMethod(method).canonical_name
        )

    pyplot.xticks(
        x,
        [
            f'{index} ({short_desc})'
            for index, short_desc in enumerate(STATEMENTS_SHORT, start=1)
        ]
    )
    pyplot.title('Average weighted NASA-TLX results')
    pyplot.ylabel('Score')
    pyplot.legend(loc='center')
    pyplot.show()
