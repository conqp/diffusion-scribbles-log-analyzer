"""Dataset-related statistics."""

from collections import defaultdict
from typing import Any

from dsla.datastructures import Dataset, ParticipantData, SelectionMethod
from dsla.statistics.selection_methods import selection_method_stats

__all__ = ['dataset_stats']


def dataset_stats(
        experiments: list[ParticipantData],
        value: str
) -> dict[Dataset, dict[SelectionMethod, Any]]:
    """Yield pairs of datasets and average correct part."""

    result = defaultdict(dict)

    for method, method_stats in selection_method_stats(experiments).items():
        for dataset, stats in method_stats['datasets'].items():
            result[dataset][method] = stats[value]

    return result
