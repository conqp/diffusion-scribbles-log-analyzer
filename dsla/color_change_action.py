"""Color changing action."""

from enum import Enum


__all__ = ['ColorChangeAction']


class ColorChangeAction(str, Enum):
    """Defines how a color was changed."""

    CLICK = 'CLICK'
    SHORTCUT = 'SHORTCUT'
