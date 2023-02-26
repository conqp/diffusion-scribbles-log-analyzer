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
                    xbar := mean(training_runs_ := [
                        len([
                            run.selection_method is method
                            for run in experiment.runs
                        ])
                        for experiment in experiments
                    ])
                ),
                'stdev': stdev(training_runs_, xbar=xbar)
            } for method in SelectionMethod
        }
    }
