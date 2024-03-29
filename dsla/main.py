"""Diffusion scribbles log analyzer."""

from argparse import ArgumentParser, Namespace
from json import dumps
from logging import DEBUG, INFO, basicConfig
from pathlib import Path

from dsla.datastructures import Dataset, Experiment
from dsla.plots import plot_age_distribution
from dsla.plots import plot_average_accuracy
from dsla.plots import plot_average_accuracy_per_method
from dsla.plots import plot_average_correct
from dsla.plots import plot_average_durations
from dsla.plots import plot_nasa_tlx
from dsla.plots import plot_self_assessment_distribution
from dsla.plots import plot_sus
from dsla.reader import read
from dsla.statistics import average_demographics
from dsla.statistics import average_sus
from dsla.statistics import average_tlx
from dsla.statistics import per_experiment_dataset_stats
from dsla.statistics import selection_method_stats
from dsla.statistics import self_assessment_distribution
from dsla.statistics import training_runs


def get_args(description: str = __doc__) -> Namespace:
    """Return the parsed command line arguments."""

    parser = ArgumentParser(description=description)
    parser.add_argument('file', type=Path, nargs='+')
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument(
        '-A', '--accuracy', action='store_true',
        help='print statistics (plots only)'
    )
    parser.add_argument(
        '-B', '--brushing-methods', action='store_true',
        help='print brushing methods statistics'
    )
    parser.add_argument(
        '-D', '--demographics', action='store_true',
        help='print demographic statistics'
    )
    parser.add_argument(
        '-E', '--dataset', metavar='dataset', type=Dataset,
        help='print dataset statistics'
    )
    parser.add_argument(
        '-N', '--nasa-tlx', action='store_true',
        help='print NASA-TLX statistics'
    )
    parser.add_argument(
        '-P', '--participants', action='store_true',
        help='print amount of participants'
    )
    parser.add_argument(
        '-S', '--self-assessment', action='store_true',
        help='print self-assessment statistics'
    )
    parser.add_argument(
        '-T', '--training', action='store_true',
        help='print training statistics'
    )
    parser.add_argument(
        '-U', '--system-usability-scale', action='store_true',
        help='print System Usability Scale statistics'
    )
    parser.add_argument(
        '-p', '--plot', action='store_true',
        help='plot data if applicable'
    )
    parser.add_argument(
        '-x', '--exclude-dataset', type=Dataset, nargs='*',
        help='exclude datasets from statistics'
    )
    return parser.parse_args()


def main():
    """Run the script."""

    args = get_args()
    basicConfig(level=DEBUG if args.debug else INFO)
    experiments = list(
        filter(
            lambda exp: exp.participant.vision_ok,
            (Experiment.from_items(read(file)) for file in args.file)
        )
    )

    if args.dataset:
        print(
            'Per-experiment dataset stats:',
            dumps(
                per_experiment_dataset_stats(args.dataset, experiments),
                indent=2
            )
        )

    if args.participants:
        print('Participants:', len(experiments))

    if args.demographics:
        print(
            'Average demographics:',
            dumps(average_demographics(experiments), indent=2)
        )

    if args.self_assessment:
        print(
            'Self-assessment:',
            dumps(self_assessment_distribution(experiments), indent=2)
        )

    if args.training:
        print(
            'Training:',
            dumps(training_runs(experiments), indent=2)
        )

    if args.brushing_methods:
        print(
            'Brushing methods:',
            dumps(
                selection_method_stats(
                    experiments,
                    exclude_datasets=set(args.exclude_dataset or [])
                ),
                indent=2
            )
        )

    if args.system_usability_scale:
        print(
            'System Usability Scale:',
            dumps(average_sus(experiments), indent=2)
        )

    if args.nasa_tlx:
        print(
            'NASA-TLX:',
            dumps(average_tlx(experiments), indent=2)
        )

    if args.plot:
        if args.accuracy:
            plot_average_accuracy(experiments)
            plot_average_accuracy_per_method(experiments)

        if args.demographics:
            plot_age_distribution(experiments)

        if args.self_assessment:
            plot_self_assessment_distribution(experiments)

        if args.brushing_methods:
            plot_average_correct(experiments)
            plot_average_durations(experiments)

        if args.system_usability_scale:
            plot_sus(experiments)

        if args.nasa_tlx:
            plot_nasa_tlx(experiments)


if __name__ == '__main__':
    main()
