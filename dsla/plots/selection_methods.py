"""Plot statistics on selection methods."""

from matplotlib import pyplot

from dsla.datastructures import Experiment
from dsla.statistics import selection_method_stats


__all__ = ['plot_average_correct', 'plot_average_durations']


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


def plot_average_durations(
        experiments: list[Experiment],
        offset: int = -0.3
) -> None:
    """Plot mean durations per brushing method and scatter plot."""

    plot_average_duration(experiments, key='draw_duration', offset=offset)
    plot_average_duration(experiments, key='task_duration', offset=offset)


def plot_per_class_accuracy(
        experiments: list[Experiment],
        offset: int = -0.3
) -> None:
    """Plot the average accuracy per brushing color."""

    for index, (method, stats) in enumerate(
            selection_method_stats(experiments).items()
    ):
        x = []
        y = []

        for clas, value in sorted(
                stats['precision'].items(),
                key=lambda item: int(item[0])
        ):
            x.append(str(clas))
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



def plot_average_duration(
        experiments: list[Experiment],
        key: str,
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
            y.append(value['summary'][key])

        pyplot.bar(
            [p + offset + index * 0.2 for p in range(len(x))],
            y,
            0.2,
            label=method.canonical_name
        )

    name = key.split('_')[0]
    pyplot.xticks(range(6), x)
    pyplot.title(f'Average {name} durations')
    pyplot.xlabel('Dataset')
    pyplot.ylabel(f'{name.capitalize()} duration in seconds')
    pyplot.legend(loc='center')
    pyplot.show()
