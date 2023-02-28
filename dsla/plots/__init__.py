"""Plotting of graphs."""

from dsla.plots.accuracy import plot_average_accuracy
from dsla.plots.accuracy import plot_average_accuracy_per_method
from dsla.plots.demographics import plot_age_distribution
from dsla.plots.demographics import plot_self_assessment_distribution
from dsla.plots.nasa_tlx import plot_nasa_tlx
from dsla.plots.selection_methods import plot_average_correct
from dsla.plots.selection_methods import plot_average_durations
from dsla.plots.system_usability_scale import plot_sus


__all__ = [
    'plot_age_distribution',
    'plot_average_accuracy',
    'plot_average_accuracy_per_method',
    'plot_average_correct',
    'plot_average_durations',
    'plot_nasa_tlx',
    'plot_self_assessment_distribution',
    'plot_sus'
]
