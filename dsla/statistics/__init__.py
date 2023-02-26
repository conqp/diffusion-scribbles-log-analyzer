"""Statistics calculation and plotting."""

from dsla.statistics.dataset import dataset_stats
from dsla.statistics.demographics import age_distribution
from dsla.statistics.demographics import average_demographics
from dsla.statistics.demographics import self_assessment_distribution
from dsla.statistics.nasa_tlx import average_tlx
from dsla.statistics.selection_methods import selection_method_stats
from dsla.statistics.system_usability_scale import average_sus
from dsla.statistics.training import training_runs


__all__ = [
    'age_distribution',
    'average_demographics',
    'average_sus',
    'average_tlx',
    'dataset_stats',
    'selection_method_stats',
    'self_assessment_distribution',
    'training_runs'
]
