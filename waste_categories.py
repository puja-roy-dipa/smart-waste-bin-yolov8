"""Map six detector classes to paper-described physical bin categories.

``non-recyclable`` is deliberately absent: it is a system-level fallback for
unrecognized items, not a seventh detector class.
"""
from __future__ import annotations
from typing import Final

RECYCLABLE: Final = "recyclable"
COMPOSTABLE: Final = "compostable"
NON_RECYCLABLE_FALLBACK: Final = "non-recyclable"
CLASS_TO_BIN: Final[dict[str, str]] = {
    "electronic": RECYCLABLE, "glass": RECYCLABLE, "metal": RECYCLABLE,
    "organic": COMPOSTABLE, "paper": RECYCLABLE, "plastic": RECYCLABLE,
}

def bin_for_detected_class(class_name: str) -> str:
    """Return a destination for a recognized class; unknowns raise KeyError.

    The system, not this detector mapping, applies the paper-described fallback.
    """
    return CLASS_TO_BIN[class_name.strip().lower()]
