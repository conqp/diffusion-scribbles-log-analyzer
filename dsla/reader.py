"""CSV file reader."""

from csv import reader
from logging import getLogger
from pathlib import Path
from typing import Iterator

from dsla.datastructures import Classification
from dsla.datastructures import CorrectClassifications
from dsla.datastructures import Event
from dsla.datastructures import NASA_TLX
from dsla.datastructures import Participant
from dsla.datastructures import Study
from dsla.datastructures import Summary
from dsla.datastructures import SystemUsabilityScale
from dsla.datastructures import Task
from dsla.datastructures import TLXAttributes


LOGGER = getLogger('parser')


def read(file: Path):
    """Read the respective file."""

    records = read_records(file)

    while True:
        try:
            record = next(records)
        except StopIteration:
            return

        if not record:
            continue

        if len(record) != 1:
            raise ValueError(f'Expected keyword but found: {record}')

        keyword = record[0]

        if keyword == 'STUDY':
            next(records)     # Discard CSV header.
            yield Study.from_csv(next(records))
        elif keyword == 'PARTICIPANT':
            next(records)     # Discard CSV header.
            yield Participant.from_csv(next(records))
        elif keyword == 'TASK':
            next(records)     # Discard CSV header.
            yield Task(parse_events(records))
        elif keyword == 'SUMMARY':
            next(records)     # Discard CSV header.
            yield Summary.from_csv(next(records))
        elif keyword == 'Classification ...':
            yield Classification(
                int(item) if item else None for item in next(records)
            )
        elif keyword == 'Correct ...':
            yield CorrectClassifications(map(bool, map(int, next(records))))
        elif keyword == 'QUESTIONS SUS':
            yield parse_sus(records)
        elif keyword == 'QUESTIONS TLX':
            yield parse_nasa_tlx(records)
        elif keyword == 'QUESTIONS TLX WEIGHTS':
            next(records)     # Discard line one.
            next(records)     # Discard line two.
            discard_empty_record(records)
        elif keyword == 'TLX WEIGHTS':
            next(records)     # Discard CSV header.
            yield TLXAttributes.from_csv(next(records))


def read_records(file: Path) -> Iterator[list[str]]:
    """Yields CSV records of the given file."""

    with file.open('r', encoding='utf-8') as file_handler:
        for line, record in enumerate(reader(file_handler), start=1):
            LOGGER.debug('#%i: %s', line, record)
            yield record


def parse_events(records: Iterator[list[str]]) -> Iterator[Event]:
    """Parse events."""

    for record in records:
        if not record:
            return

        yield Event.from_csv(record)


def discard_empty_record(records: Iterator[list[str]]) -> None:
    """Discard an empty record."""

    if record := next(records):
        raise ValueError(f'Expected empty record but found: {record}')


def parse_sus(records: Iterator[list[str]]) -> SystemUsabilityScale:
    """Parse the SUS questionnaire."""

    next(records)  # Discard CSV header.
    raw = next(records)
    weighted = next(records)
    discard_empty_record(records)

    if len(record := next(records)) != 1 and record[0] != 'score':
        raise ValueError(f'Expected score. Found {record}')

    pre_calculated_score = float(next(records)[0])
    return SystemUsabilityScale.from_csvs(raw, weighted, pre_calculated_score)


def parse_nasa_tlx(records: Iterator[list[str]]) -> NASA_TLX:
    """Parse NASA TLX questionnaires."""

    next(records)  # Discard CSV header.
    tlx = next(records)
    tlx_weighed = next(records)
    discard_empty_record(records)

    if len(record := next(records)) != 1 and record[0] != 'score':
        raise ValueError(f'Expected score. Found {record}')

    score = float(next(records)[0])
    return NASA_TLX.from_csvs(tlx, tlx_weighed, score=score)
