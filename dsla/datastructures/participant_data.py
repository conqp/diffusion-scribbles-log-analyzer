"""Per-participant study data."""

from __future__ import annotations
from typing import Any, Iterator, NamedTuple

from dsla.datastructures.event import TrainingTaskStart
from dsla.datastructures.nasa_tlx import TLXAttributes
from dsla.datastructures.participant import Participant
from dsla.datastructures.selection_method_run import SelectionMethodRun
from dsla.datastructures.study import Study
from dsla.datastructures.task import Task


__all__ = ['ParticipantData']


class ParticipantData(NamedTuple):
    """Per-participant study data."""

    study: Study
    participant: Participant
    tlx_weights: TLXAttributes
    runs: list[SelectionMethodRun]

    @classmethod
    def from_items(cls, items: Iterator[Any]) -> ParticipantData:
        """Creates participant data from an iterable of objects."""

        study, participant, *remainder = items

        if not isinstance(study, Study):
            raise ValueError('Expected study as first item.')

        if not isinstance(participant, Participant):
            raise ValueError('Expected participant as second item.')

        tlx_attributes = [
            item for item in remainder if isinstance(item, TLXAttributes)
        ]

        if len(tlx_attributes) != 1:
            raise ValueError('Expected exactly one TLX attributes instance.')

        return cls(
            study,
            participant,
            tlx_attributes[0],
            list(parse_selection_method_runs(
                item for item in remainder
                if not isinstance(item, TLXAttributes)
            ))
        )


def parse_selection_method_runs(
        items: Iterator[Any]
) -> Iterator[SelectionMethodRun]:
    """Parse selection method runs."""

    params = []
    current_method = None

    for item in items:
        if isinstance(item, Task):
            for event in item:
                if isinstance(event, TrainingTaskStart):
                    if current_method is None:
                        current_method = event.selection_method
                    elif current_method != event.selection_method:
                        yield SelectionMethodRun.from_items(
                            params, current_method
                        )
                        current_method = event.selection_method
                        params.clear()

        params.append(item)

    if params:
        yield SelectionMethodRun.from_items(params, current_method)
