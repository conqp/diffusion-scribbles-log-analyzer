"""Scribble statistics."""

from statistics import mean
from typing import Any

from dsla.datastructures import STUDY_DATASETS
from dsla.datastructures import ParticipantData
from dsla.datastructures import SelectionMethod
from dsla.datastructures import Summary


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
            'summary': mean_summary(
                [
                    task.summary
                    for experiment in experiments
                    for run in experiment.runs
                    for task in run.tasks
                    if run.selection_method is method
                ]
            ),
            'correct': (correct := mean(
                sum(task.correct)
                for experiment in experiments
                for run in experiment.runs
                for task in run.tasks
                if run.selection_method is method
            )),
            'wrong': (wrong := mean(
                sum(not correct for correct in task.correct)
                for experiment in experiments
                for run in experiment.runs
                for task in run.tasks
                if run.selection_method is method
            )),
            'correct_pct': correct / (correct + wrong),
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
                    'correct_pct': correct_dataset / (
                            correct_dataset + wrong_dataset
                    ),
                } for dataset in STUDY_DATASETS
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
