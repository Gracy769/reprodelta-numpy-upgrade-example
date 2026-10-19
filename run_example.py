"""Run the constructed signal classifier with the installed NumPy version."""

from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).parent / "fixture" / "project"))
from pipeline import classify_signal  # noqa: E402


if __name__ == "__main__":
    signal = np.array([1.0] * 7 + [1.0000001192092896], dtype=np.float32)
    print(classify_signal(signal))
