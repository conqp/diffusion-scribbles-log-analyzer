"""Evaluation of the System Usability Scale questionnaires."""

from statistics import mean
from typing import Any

from dsla.datastructures import Experiment
from dsla.datastructures import SelectionMethod
from dsla.datastructures import SystemUsabilityScale

__all__ = ['average_sus']


def average_sus(experiments: list[Experiment]) -> dict[str, Any]:
    """Return average data of the SUSs."""

    return {
        method: mean_sus([
            run.system_usability_scale
            for experiment in experiments
            for run in experiment.runs
            if run.selection_method is method
        ])
        for method in SelectionMethod
    }


def mean_sus(suss: list[SystemUsabilityScale]) -> dict[str, Any]:
    """Returns the mean SUS."""

    return {
        'questionnaire': {
            'use_frequently': mean(
                sus.questionnaire.use_frequently for sus in suss
            ),
            'too_complex': mean(sus.questionnaire.too_complex for sus in suss),
            'easy_to_use': mean(sus.questionnaire.easy_to_use for sus in suss),
            'tech_support_required': mean(
                sus.questionnaire.tech_support_required for sus in suss
            ),
            'well_integrated': mean(
                sus.questionnaire.well_integrated for sus in suss
            ),
            'too_inconsistent': mean(
                sus.questionnaire.too_inconsistent for sus in suss
            ),
            'easy_to_learn': mean(
                sus.questionnaire.easy_to_learn for sus in suss
            ),
            'cumbersome': mean(sus.questionnaire.cumbersome for sus in suss),
            'confident': mean(sus.questionnaire.confident for sus in suss),
            'much_learning_required': mean(
                sus.questionnaire.much_learning_required for sus in suss
            )
        },
        'scores': {
            'use_frequently': mean(sus.scores.use_frequently for sus in suss),
            'too_complex': mean(sus.scores.too_complex for sus in suss),
            'easy_to_use': mean(sus.scores.easy_to_use for sus in suss),
            'tech_support_required': mean(
                sus.scores.tech_support_required for sus in suss
            ),
            'well_integrated': mean(
                sus.scores.well_integrated for sus in suss
            ),
            'too_inconsistent': mean(
                sus.scores.too_inconsistent for sus in suss
            ),
            'easy_to_learn': mean(sus.scores.easy_to_learn for sus in suss),
            'cumbersome': mean(sus.scores.cumbersome for sus in suss),
            'confident': mean(sus.scores.confident for sus in suss),
            'much_learning_required': mean(
                sus.scores.much_learning_required for sus in suss
            )
        },
        'pre_calculated_score': mean(sus.pre_calculated_score for sus in suss),
        'score': mean(sus.score for sus in suss)
    }
