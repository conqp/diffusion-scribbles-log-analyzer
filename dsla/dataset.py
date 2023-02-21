"""Datasets."""

from enum import Enum


__all__ = ['Dataset']


class Dataset(str, Enum):
    """Available datasets."""

    # Training
    R15 = '10_R15'

    # Study
    GAUSSIAN = '1_Gaussian'
    PATH_BASED = '2_pathbased'
    CRIM_RAD = '3_CRIM_RAD'
    RAD_PTRATIO = '4_RAD_PTRATIO'
    INDUS_NOX = '5_INDUS_NOX'
    AGE_DIS = '6_AGE_DIS'
