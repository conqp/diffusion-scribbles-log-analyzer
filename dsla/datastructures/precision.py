"""Representation of precision information."""

from __future__ import annotations
from typing import Iterator, NamedTuple

from dsla.datastructures.classification import Classification


__all__ = ['Precision']


class Precision(NamedTuple):
    """Selection precisions."""

    true_positives: int
    false_positives: int
    true_negatives: int
    false_negatives: int

    @classmethod
    def from_classification(
            cls,
            classification: Classification,
            solution: list[int]
    ) -> Iterator[tuple[int, Precision]]:
        """Calculate precisions from classification."""
        if len(classification) != len(solution):
            raise ValueError(
                'Length of classifications does not match length of solution.'
            )

        for clas in range(3):   # 0, 1, 2
            tp = fp = tn = fn = 0

            for actual, target in zip(classification, solution):
                if target == clas:
                    if actual == clas:
                        tp += 1
                    else:
                        fn += 1
                else:
                    if actual == clas:
                        fp += 1
                    else:
                        tn += 1

            yield clas, cls(tp, fp, tn, fn)
