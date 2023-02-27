"""Miscellaneous functions."""

__all__ = ['dict_to_kv']


def dict_to_kv(dct: dict) -> tuple[list, list]:
    """Convert a dict into two lists of keys and values."""

    keys = []
    values = []

    for key, value in dct.items():
        keys.append(key)
        values.append(value)

    return keys, values
