# -*- coding: utf-8 -*-
"""
Pure-Python fallback for RadarGridC (Cython extension).

Repo 222 ships RadarGridC.pyx which requires compilation (see setup.py cythonize).
If the compiled extension is not available, this module provides compatible
APIs by re-exporting implementations from RadarGrid.py.
D:\pycwr\pycwr\core\RadarGridC.py
"""

from .RadarGrid import (
    get_CR_xy,
    get_CAPPI_xy,
    ppi_to_grid,
    interp_ppi,
    interp_azimuth,
)

__all__ = [
    "get_CR_xy",
    "get_CAPPI_xy",
    "ppi_to_grid",
    "interp_ppi",
    "interp_azimuth",
]
