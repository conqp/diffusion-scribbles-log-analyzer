"""Datasets."""

from enum import Enum

from dsla.solutions import SOLUTIONS


__all__ = ['STUDY_DATASETS', 'Dataset']


class Dataset(str, Enum):
    """Available datasets."""

    # Study
    A = '3_CRIM_RAD'
    B = '5_INDUS_NOX'
    C = '4_RAD_PTRATIO'
    D = '6_AGE_DIS'
    E = '1_Gaussian'
    F = '2_pathbased'
    # Training
    PERSONAL_HIKING_DATA = '7_personalHikingData'
    AGGREGATION = '8_Aggregation'
    R15 = '10_R15'
    SIMPLIFIED_IRIS = '12_simplified.iris.data.set'

    @property
    def solution(self) -> list[int]:
        """Solutions of this dataset."""
        return SOLUTIONS[self.value]


STUDY_DATASETS = {
    Dataset.A,
    Dataset.B,
    Dataset.C,
    Dataset.D,
    Dataset.E,
    Dataset.F
}
