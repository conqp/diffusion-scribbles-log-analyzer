"""Diffusion scribbles log analyzer."""

from argparse import ArgumentParser, Namespace
from logging import DEBUG, INFO, basicConfig
from pathlib import Path

from dsla.reader import read
from dsla.participant_data import ParticipantData


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

    for file in args.file:
        print('Parsing file:', file)
        participant_data = ParticipantData.from_items(read(file))
        print(participant_data)
        print('Runs:', len(participant_data.runs))


if __name__ == '__main__':
    main()
