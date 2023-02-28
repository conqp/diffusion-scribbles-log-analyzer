"""Scribble statistics."""

from statistics import mean
from typing import Any

from dsla.datastructures import STUDY_DATASETS
from dsla.datastructures import Dataset
from dsla.datastructures import Experiment
from dsla.datastructures import Precision
from dsla.datastructures import SelectionMethod
from dsla.datastructures import Summary


__all__ = ['selection_method_stats']


def selection_method_stats(
        experiments: list[Experiment],
        *,
        exclude_datasets: set[Dataset] = frozenset()
) -> dict[SelectionMethod, Any]:
    """Returns statistics about the scribbling processes."""

    return {
        method: {
            'mean_processed_scatter_plots': mean(
                len([
                    task for task in run.tasks
                    if task.dataset not in exclude_datasets
                ])
                for experiment in experiments
                for run in experiment.runs
            ),
            'summary': mean_summary(
                [
                    task.summary
                    for experiment in experiments
                    for run in experiment.runs
                    for task in run.tasks
                    if run.selection_method is method
                    and task.dataset not in exclude_datasets
                ]
            ),
            'correct': (correct := mean(
                sum(task.correct)
                for experiment in experiments
                for run in experiment.runs
                for task in run.tasks
                if run.selection_method is method
                and task.dataset not in exclude_datasets
            )),
            'wrong': (wrong := mean(
                sum(not correct for correct in task.correct)
                for experiment in experiments
                for run in experiment.runs
                for task in run.tasks
                if run.selection_method is method
                and task.dataset not in exclude_datasets
            )),
            'precision': {
                clas: mean_precision(
                    [
                        precision
                        for experiment in experiments
                        for run in experiment.runs
                        for task in run.tasks
                        for clas_, precision in task.precisions
                        if run.selection_method is method
                        and task.dataset not in exclude_datasets
                        and clas_ == clas
                        and precision.positives > 0
                    ]
                ) for clas in range(3)
            },
            'correct_pct': correct / (correct + wrong),
            'datasets': {
                dataset: {
                    'events': mean(
                        len(task.events)
                        for experiment in experiments
                        for run in experiment.runs
                        for task in run.tasks
                        if run.selection_method is method
                        and task.dataset is dataset
                    ),
                    'summary': mean_summary(
                        [
                            task.summary
                            for experiment in experiments
                            for run in experiment.runs
                            for task in run.tasks
                            if run.selection_method is method
                            and task.dataset is dataset
                        ]
                    ),
                    'correct': (correct_dataset := mean(
                        sum(task.correct)
                        for experiment in experiments
                        for run in experiment.runs
                        for task in run.tasks
                        if run.selection_method is method
                        and task.dataset is dataset
                    )),
                    'wrong': (wrong_dataset := mean(
                        sum(not correct for correct in task.correct)
                        for experiment in experiments
                        for run in experiment.runs
                        for task in run.tasks
                        if run.selection_method is method
                        and task.dataset is dataset
                    )),
                    'precision': {
                        clas: mean_precision(
                            [
                                precision
                                for experiment in experiments
                                for run in experiment.runs
                                for task in run.tasks
                                for clas_, precision in task.precisions
                                if run.selection_method is method
                                and task.dataset is dataset
                                and clas_ == clas
                                and precision.positives > 0
                            ]
                        ) for clas in range(3)
                    },
                    'correct_pct': correct_dataset / (
                            correct_dataset + wrong_dataset
                    ),
                } for dataset in filter(
                    lambda dataset: dataset not in exclude_datasets,
                    STUDY_DATASETS
                )
            }
        } for method in SelectionMethod
    }


def mean_summary(summaries: list[Summary]) -> dict[str, Any]:
    """Average task summaries."""

    return {
        'task_duration': mean(
            summary.task_duration.total_seconds() for summary in summaries
        ),
        'draw_duration': mean(
            summary.draw_duration.total_seconds() for summary in summaries
        ),
        'invert_count': mean(summary.invert_count for summary in summaries),
        'undo_count': mean(summary.undo_count for summary in summaries),
        'redo_count': mean(summary.redo_count for summary in summaries),
        'reset_count': mean(summary.reset_count for summary in summaries),
        'scribble_count': mean(
            summary.scribble_count for summary in summaries
        ),
        'scribble_pixels': mean(
            summary.scribble_pixels for summary in summaries
        ),
        'eraser_count': mean(summary.eraser_count for summary in summaries),
    }


def mean_precision(precisions: list[Precision]) -> dict[str, float] | None:
    """Return the mean precision."""

    if not precisions:
        return None

    return {
        'true_positives_pct': mean(
            precision.true_positives_pct for precision in precisions
        ),
        'false_positives_pct': mean(
            precision.false_positives_pct for precision in precisions
        ),
        'true_negatives_pct': mean(
            precision.true_negatives_pct for precision in precisions
        ),
        'false_negatives_pct': mean(
            precision.false_negatives_pct for precision in precisions
        )
    }
