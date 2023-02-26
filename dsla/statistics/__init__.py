"""Statistics calculation and plotting."""

from dsla.statistics.demographics import age_distribution, average_demographics
from dsla.statistics.nasa_tlx import average_tlx
from dsla.statistics.scribble import scribble_stats
from dsla.statistics.system_usability_scale import average_sus
from dsla.statistics.training import training_runs

__all__ = [
    'age_distribution',
    'average_demographics',
    'average_sus',
    'average_tlx',
    'scribble_stats',
    'training_runs'
]
