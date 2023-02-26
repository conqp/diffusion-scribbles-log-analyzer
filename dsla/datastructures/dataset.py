"""Datasets."""

from enum import Enum


__all__ = ['STUDY_DATASETS', 'Dataset']


class Dataset(str, Enum):
    """Available datasets."""

    # Study
    GAUSSIAN = '1_Gaussian'
    PATH_BASED = '2_pathbased'
    CRIM_RAD = '3_CRIM_RAD'
    RAD_PTRATIO = '4_RAD_PTRATIO'
    INDUS_NOX = '5_INDUS_NOX'
    AGE_DIS = '6_AGE_DIS'
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
