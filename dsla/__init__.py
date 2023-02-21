"""Diffusion scribbles log analyzer."""

from argparse import ArgumentParser, Namespace
from pathlib import Path

from dsla.reader import read


def get_args(description: str = __doc__) -> Namespace:
    """Return the parsed command line arguments."""

    parser = ArgumentParser(description=description)
    parser.add_argument('file', type=Path, nargs='+')
    return parser.parse_args()


def main():
    """Run the script."""

    args = get_args()

    for file in args.file:
        print('Parsing file:', file)

        for item in read(file):
            print(item)


if __name__ == '__main__':
    main()
