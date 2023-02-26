"""Statistics on the NASA-TLX questionnaire."""

from statistics import mean
from typing import Any

from dsla.datastructures import NASA_TLX
from dsla.datastructures import ParticipantData
from dsla.datastructures import SelectionMethod
from dsla.datastructures import TLXAttributes

__all__ = ['average_tlx']


def average_tlx(experiments: list[ParticipantData]) -> dict[str, Any]:
    """Return mean NASA-TLX data."""

    return {
        'weighting': mean_weighting([
            experiment.tlx_weights
            for experiment in experiments
        ]),
        **{
            selection_method: mean_tlx([
                run.nasa_tlx
                for experiment in experiments
                for run in experiment.runs
                if run.selection_method is selection_method
            ]) for selection_method in SelectionMethod
        }
    }


def mean_weighting(weightings: list[TLXAttributes]) -> dict[str, Any]:
    """Return the mean NASA-TLX weightings."""

    return {
        'mental_demand': mean(
            weighting.mental_demand for weighting in weightings
        ),
        'physical_demand': mean(
            weighting.physical_demand for weighting in weightings
        ),
        'temporal_demand': mean(
            weighting.temporal_demand for weighting in weightings
        ),
        'overall_performance': mean(
            weighting.overall_performance for weighting in weightings
        ),
        'effort': mean(weighting.effort for weighting in weightings),
        'frustration_level': mean(
            weighting.frustration_level for weighting in weightings
        )
    }


def mean_tlx(nasa_tlxs: list[NASA_TLX]) -> dict[str, Any]:
    """Return mean TLX data."""

    return {
        'raw': {
            'mental_demand': mean(
                nasa_tlx.raw.mental_demand for nasa_tlx in nasa_tlxs
            ),
            'physical_demand': mean(
                nasa_tlx.raw.physical_demand for nasa_tlx in nasa_tlxs
            ),
            'temporal_demand': mean(
                nasa_tlx.raw.temporal_demand for nasa_tlx in nasa_tlxs
            ),
            'overall_performance': mean(
                nasa_tlx.raw.overall_performance for nasa_tlx in nasa_tlxs
            ),
            'effort': mean(nasa_tlx.raw.effort for nasa_tlx in nasa_tlxs),
            'frustration_level': mean(
                nasa_tlx.raw.frustration_level for nasa_tlx in nasa_tlxs
            )
        },
        'weighted': {
            'mental_demand': mean(
                nasa_tlx.weighted.mental_demand for nasa_tlx in nasa_tlxs
            ),
            'physical_demand': mean(
                nasa_tlx.weighted.physical_demand for nasa_tlx in nasa_tlxs
            ),
            'temporal_demand': mean(
                nasa_tlx.weighted.temporal_demand for nasa_tlx in nasa_tlxs
            ),
            'overall_performance': mean(
                nasa_tlx.weighted.overall_performance for nasa_tlx in nasa_tlxs
            ),
            'effort': mean(nasa_tlx.weighted.effort for nasa_tlx in nasa_tlxs),
            'frustration_level': mean(
                nasa_tlx.weighted.frustration_level for nasa_tlx in nasa_tlxs
            )
        },
        'score': mean(nasa_tlx.score for nasa_tlx in nasa_tlxs)
    }
