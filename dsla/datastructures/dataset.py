"""Datasets."""

from enum import Enum


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


STUDY_DATASETS = {
    Dataset.GAUSSIAN,
    Dataset.PATH_BASED,
    Dataset.CRIM_RAD,
    Dataset.RAD_PTRATIO,
    Dataset.INDUS_NOX,
    Dataset.AGE_DIS
}
