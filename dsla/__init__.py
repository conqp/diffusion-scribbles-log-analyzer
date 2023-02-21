"""Diffusion scribbles log analyzer."""

from argparse import ArgumentParser, Namespace
from logging import DEBUG, INFO, basicConfig
from pathlib import Path

from dsla.reader import read


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

        for item in read(file):
            print(item)


if __name__ == '__main__':
    main()
