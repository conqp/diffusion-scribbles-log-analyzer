"""Plotting of accuracy."""

from typing import Any

from matplotlib import pyplot

from dsla.datastructures import Experiment, SelectionMethod
from dsla.statistics import selection_method_stats


__all__ = ['plot_average_accuracy', 'plot_average_accuracy_per_method']


def plot_average_accuracy(
        experiments: list[Experiment],
        offset: int = -0.3
) -> None:
    """Plot the average precision per selection method."""

    for index, (method, stats) in enumerate(
            selection_method_stats(experiments).items()
    ):
        x = []
        y = []

        for typ, value in stats['precision'].items():
            x.append(' '.join(typ.split('_')[:2]))
            y.append(value)

        pyplot.bar(
            [p + offset + index * 0.2 for p in range(len(x))],
            y,
            0.2,
            label=method.canonical_name
        )

    pyplot.xticks(range(4), x)
    pyplot.title('Selection accuracy')
    pyplot.ylabel('Amount in %')
    pyplot.legend(loc='center')
    pyplot.show()


def plot_average_accuracy_per_method(
        experiments: list[Experiment],
        bar_width: float = 0.2
) -> None:
    """Plot the average precision per selection method."""

    for index, (method, stats) in enumerate(
            selection_method_stats(experiments).items()
    ):
        plot_accuracy_for_method(method, stats, bar_width=bar_width)


def plot_accuracy_for_method(
        method: SelectionMethod,
        stats: dict[str, Any],
        bar_width: float = 0.2
) -> None:
    """Plot accuracy details for the given selection method."""

    for index, (dataset, values) in enumerate(
            sorted(
                stats['datasets'].items(),
                key=lambda item: item[0].name
            )
    ):
        x = []
        y = []

        for typ, value in values['precision'].items():
            x.append(' '.join(typ.split('_')[:2]))
            y.append(value)

        offset = - (bar_width * len(x) / 2 - bar_width / 2)
        pyplot.bar(
            [p + offset + index * bar_width for p in range(len(x))],
            y,
            bar_width,
            label=f'dataset {dataset.name}'
        )

    pyplot.xticks(range(4), x)
    pyplot.title(
        f'Selection accuracy for {method.canonical_name.capitalize()}'
    )
    pyplot.ylabel('Amount in %')
    pyplot.legend(loc='center')
    pyplot.show()
