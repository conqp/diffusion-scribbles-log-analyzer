"""Training statistics."""

from statistics import mean, stdev
from typing import Any

from dsla.datastructures import ParticipantData
from dsla.datastructures import SelectionMethod


__all__ = ['training_runs']


def training_runs(
        experiments: list[ParticipantData]
) -> dict[str, Any]:
    """Return a dict of average demographics."""

    return {
        'training_runs': {
            method: {
                'mean': (
                    xbar := mean(training_runs_per_experiment_and_method := [
                        len(run.training)
                        for experiment in experiments
                        for run in experiment.runs
                        if run.selection_method is method
                    ])
                ),
                'stdev': stdev(
                    training_runs_per_experiment_and_method,
                    xbar=xbar
                )
            } for method in SelectionMethod
        }
    }
