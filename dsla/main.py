"""Diffusion scribbles log analyzer."""

from argparse import ArgumentParser, Namespace
from json import dumps
from logging import DEBUG, INFO, basicConfig
from pathlib import Path

from dsla.datastructures import ParticipantData
from dsla.reader import read
from dsla.statistics import average_demographics
from dsla.statistics import average_sus
from dsla.statistics import average_tlx
from dsla.statistics import scribble_stats
from dsla.statistics import training_runs


def get_args(description: str = __doc__) -> Namespace:
    """Return the parsed command line arguments."""

    parser = ArgumentParser(description=description)
    parser.add_argument('file', type=Path, nargs='+')
    parser.add_argument('-d', '--debug', action='store_true')
    return parser.parse_args()


def main():
    """Run the script."""

    args = get_args()
    basicConfig(level=DEBUG if args.debug else INFO)
    experiments = [
        ParticipantData.from_items(read(file)) for file in args.file
    ]

    for experiment in experiments:
        if not experiment.participant.vision_ok:
            print('Uncorrected vision:', experiment.participant)

    print(
        'Average demographics:',
        dumps(average_demographics(experiments), indent=2)
    )
    print(
        'Training:',
        dumps(training_runs(experiments), indent=2)
    )
    print(
        'Scribbles:',
        dumps(scribble_stats(experiments), indent=2)
    )
    print(
        'System Usability Scale:',
        dumps(average_sus(experiments), indent=2)
    )
    print(
        'NASA-TLX:',
        dumps(average_tlx(experiments), indent=2)
    )


if __name__ == '__main__':
    main()
