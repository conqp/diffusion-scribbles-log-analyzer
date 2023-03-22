"""Dataset-related statistics."""

from collections import defaultdict
from typing import Any

from dsla.datastructures import Dataset, Experiment, SelectionMethod
from dsla.statistics.selection_methods import selection_method_stats

__all__ = ['dataset_stats', 'per_experiment_dataset_stats']


def per_experiment_dataset_stats(
        dataset: Dataset,
        experiments: list[Experiment]
) -> list[dict[str, Any]]:
    """Returns stats of the given dataset."""

    return [
        {
            'study': experiment.study.to_json(),
            'participant': experiment.participant.to_json(),
            'runs': [
                {
                    'selection_method': run.selection_method,
                    'tasks': [
                        task.to_json()
                        for task in run.tasks
                        #if task.dataset is dataset
                    ]
                }
                for run in experiment.runs
            ]
        }
        for experiment in experiments
    ]


def dataset_stats(
        experiments: list[Experiment],
        value: str
) -> dict[Dataset, dict[SelectionMethod, Any]]:
    """Yield pairs of datasets and average correct part."""

    result = defaultdict(dict)

    for method, method_stats in selection_method_stats(experiments).items():
        for dataset, stats in method_stats['datasets'].items():
            result[dataset][method] = stats[value]

    return result
