"""Scribble statistics."""

from typing import Any
from statistics import mean

from dsla.datastructures import STUDY_DATASETS
from dsla.datastructures import ParticipantData
from dsla.datastructures import SelectionMethod


__all__ = ['scribble_stats']


def scribble_stats(experiments: list[ParticipantData]) -> dict[str, Any]:
    """Returns statistics about the scribbling processes."""

    return {
        method: {
            'mean_processed_scatter_plots': mean(
                len(run.tasks)
                for experiment in experiments
                for run in experiment.runs
            ),
            **{
                dataset: {
                    'events': mean(
                        len(task.events)
                        for experiment in experiments
                        for run in experiment.runs
                        for task in run.tasks
                        if run.selection_method is method
                        and task.dataset is dataset
                    ),
                } for dataset in STUDY_DATASETS
            }
        } for method in SelectionMethod
    }
