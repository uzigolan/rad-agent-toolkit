from .base import RadDriver
from .etx1p import Etx1pDriver
from .etx2 import Etx2Driver
from .mp4100 import Mp4100Driver
from .secflow import SecFlowDriver

_DRIVERS: dict[str, RadDriver] = {
    "etx1p": Etx1pDriver(),
    "etx2": Etx2Driver(),
    "mp4100": Mp4100Driver(),  # shared dialect + candidate-DB commit (see driver docstring)
    "secflow": SecFlowDriver(),
    # Planned families (different CLI dialects — need their own driver base):
    #   "etx1"    — legacy ETX-1 line (menu CLI; ETX-1p is NOT this — it's context-based)
}


def get_driver(family: str) -> RadDriver:
    if family not in _DRIVERS:
        known = ", ".join(sorted(_DRIVERS))
        raise KeyError(f"No driver for family '{family}'. Available: {known}")
    return _DRIVERS[family]
