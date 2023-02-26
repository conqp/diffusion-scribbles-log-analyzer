"""Statistics calculation and plotting."""

from dsla.statistics.demographics import average_demographics
from dsla.statistics.scribble import scribble_stats
from dsla.statistics.system_usability_scale import average_sus
from dsla.statistics.training import training_runs


__all__ = [
    'average_demographics',
    'average_sus',
    'scribble_stats',
    'training_runs'
]
