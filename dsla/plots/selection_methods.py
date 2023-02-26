"""Plot statistics on selection methods."""

from dsla.datastructures import ParticipantData
from dsla.statistics import selection_method_stats


__all__ = ['plot_average_method_performance_on_plots']


def plot_average_method_performance_on_plots(
        experiments: list[ParticipantData]
) -> None:
    """Plot mean performance data per brushing method and scatter plot."""

    for method, method_stats in selection_method_stats(experiments).items():
        for dataset, dataset_stats in method_stats['datasets'].items():
            raise NotImplementedError()
