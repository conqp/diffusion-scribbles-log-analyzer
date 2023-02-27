"""Plot statistics on selection methods."""

from matplotlib import pyplot

from dsla.datastructures import Experiment
from dsla.statistics import selection_method_stats


__all__ = ['plot_average_correct']


def plot_average_correct(
        experiments: list[Experiment],
        offset: int = -0.3
) -> None:
    """Plot mean performance data per brushing method and scatter plot."""

    for index, (method, stats) in enumerate(
            selection_method_stats(experiments).items()
    ):
        x = []
        y = []

        for dataset, value in sorted(
                stats['datasets'].items(),
                key=lambda item: item[0].name
        ):
            x.append(dataset.name)
            y.append(value['correct_pct'] * 100)

        pyplot.bar(
            [p + offset + index * 0.2 for p in range(len(x))],
            y,
            0.2,
            label=method.canonical_name
        )

    pyplot.xticks(range(6), x)
    pyplot.title('Correct selections')
    pyplot.xlabel('Dataset')
    pyplot.ylabel('Correct selections in %')
    pyplot.legend(loc='center')
    pyplot.show()
