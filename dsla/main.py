"""Diffusion scribbles log analyzer."""

from argparse import ArgumentParser, Namespace
from json import dumps
from logging import DEBUG, INFO, basicConfig
from pathlib import Path

from dsla.reader import read
from dsla.datastructures import ParticipantData
from dsla.statistics import average_demographics, training_runs


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


if __name__ == '__main__':
    main()
