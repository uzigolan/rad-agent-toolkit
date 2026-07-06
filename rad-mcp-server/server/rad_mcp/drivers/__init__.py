from .base import RadDriver
from .etx2 import Etx2Driver
from .secflow import SecFlowDriver

_DRIVERS: dict[str, RadDriver] = {
    "etx2": Etx2Driver(),
    "secflow": SecFlowDriver(),
    # Planned families (different CLI dialects — need their own driver base):
    #   "etx1"    — legacy ETX-1 line
    #   "mp4100"  — Megaplex-4100 multiservice access node
}


def get_driver(family: str) -> RadDriver:
    if family not in _DRIVERS:
        known = ", ".join(sorted(_DRIVERS))
        raise KeyError(f"No driver for family '{family}'. Available: {known}")
    return _DRIVERS[family]
