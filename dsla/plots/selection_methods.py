"""Plot statistics on selection methods."""

from matplotlib import pyplot

from dsla.datastructures import ParticipantData
from dsla.statistics import selection_method_stats

__all__ = ['plot_average_correct']


def plot_average_correct(
        experiments: list[ParticipantData],
        offset: int = -0.3
) -> None:
    """Plot mean performance data per brushing method and scatter plot."""

    for index, (method, stats) in enumerate(
            selection_method_stats(experiments).items()
    ):
        x = [dataset.name for dataset in stats['datasets'].keys()]
        y = [
            value['correct_pct'] * 100 for value in stats['datasets'].values()
        ]
        pyplot.bar(
            [p + offset + index * 0.2 for p in range(len(x))],
            y,
            0.2,
            label=method.name
        )

    pyplot.xticks(range(6), x)
    pyplot.title('Correct selections')
    pyplot.ylabel('Correct selections in %')
    pyplot.legend()
    pyplot.show()
