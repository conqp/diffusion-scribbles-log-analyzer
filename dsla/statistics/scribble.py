"""Scribble statistics."""

from typing import Any
from statistics import mean

from dsla.datastructures import ParticipantData, SelectionMethod


__all__ = ['scribble_stats']


def scribble_stats(experiments: list[ParticipantData]) -> dict[str, Any]:
    """Returns statistics about the scribbling processes."""

    return {
        method: {
            'mean_processed_scatter_plots': mean(
                len(run.tasks)
                for experiment in experiments
                for run in experiment.runs
            )
        } for method in SelectionMethod
    }
