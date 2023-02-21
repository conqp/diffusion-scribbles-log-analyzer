"""Diffusion scribbles log analyzer."""

from argparse import ArgumentParser, Namespace
from logging import DEBUG, INFO, basicConfig
from operator import not_
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
        # print(participant_data)
        print('Participant:', participant_data.participant)
        print('Runs:', len(participant_data.runs))

        for run in participant_data.runs:
            print('Selection method:', run.selection_method)
            print('Training runs:', len(run.training))
            print('Study runs:', len(run.tasks))
            for task in run.tasks:
                print('Dataset:', task.dataset)
                print('Correct:', sum(task.correct))
                print('Wrong:', sum(map(not_, task.correct)))


if __name__ == '__main__':
    main()
