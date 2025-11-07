from typing import List

import sysconfig
from pathlib import Path
import os
import sys

import ROOT

from .calibration import test_calibration
from .display import test_display
from .fit import test_fit
from .mfile_root import test_mfile_root

libraries = ["calibration", "display", "fit", "mfile-root"]

def load_libraries(libs : List[str]) -> None:
    libray_path : str = os.path.join(sysconfig.get_paths()["platlib"], __package__, "lib")
    print("  Add Path %s" % libray_path)
    ROOT.gSystem.SetDynamicPath(libray_path + os.pathsep + ROOT.gSystem.GetDynamicPath())
    ROOT.gSystem.SetIncludePath(libray_path + os.pathsep + ROOT.gSystem.GetIncludePath())
    
    libfmt = {
        "linux" : "lib%s.so",
        "darwin": "lib%s.dylib",
        "win32" :    "%s.dll",
    }[sys.platform]

    for lib in libs:
        if ROOT.gSystem.Load(libfmt % lib) < 0:
            raise RuntimeError("Failed to load %s", (libfmt % lib))
        else:
            print("  Loaded %s" % lib)


def main() -> None:    
    print("tv-tuner -- hdtv test application")
    print()
    print("LOAD ROOTEXT")
    try:
        load_libraries(libraries)
    except Exception as e:
        print(e)
        print("LOAD ROOTEXT - FAILED")
        exit(1)
    print("LOAD ROOTEXT - SUCCESS")
    print()
    
    print("TEST CALIBRATION")
    try:
        test_calibration()
    except Exception as e:
        print(e)
        print("TEST CALIBRATION - FAILED")
        exit(2)
    print("TEST CALIBRATION - SUCCESS")
    print()

    print("TEST DISPLAY")
    try:
        test_display()
    except Exception as e:
        print(e)
        print("TEST DISPLAY - FAILED")
        exit(2)
    print("TEST DISPLAY - SUCCESS")
    print()

    print("TEST FIT")
    try:
        test_fit()
    except Exception as e:
        print(e)
        print("TEST FIT - FAILED")
        exit(2)
    print("TEST FIT - SUCCESS")
    print()

    
    print("TEST MFILE-ROOT")
    try:
        test_mfile_root()
    except Exception as e:
        print(e)
        print("TEST MFILE-ROOT - FAILED")
        exit(2)
    print("TEST MFILE-ROOT - SUCCESS")
    print()

    print("OK")
