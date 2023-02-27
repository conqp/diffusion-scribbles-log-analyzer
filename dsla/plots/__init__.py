"""Plotting of graphs."""

from dsla.plots.demographics import plot_age_distribution
from dsla.plots.demographics import plot_self_assessment_distribution
from dsla.plots.selection_methods import plot_average_correct
from dsla.plots.system_usability_scale import plot_selection_method


__all__ = [
    'plot_age_distribution',
    'plot_average_correct',
    'plot_self_assessment_distribution',
    'plot_selection_method'
]
