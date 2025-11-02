from typing import List

import sysconfig
from pathlib import Path
import os
import sys
import time

import ROOT

ok : bool = True


libs = ["calibration", "display", "fit", "mfile-root"]

def load_lib(libs : List[str]) -> None:
    """
        Load the plugin libraries in ROOT
    """
    libfmt = {
        "linux" : "lib%s.so",
        "darwin": "lib%s.dylib",
        "win32" :    "%s.dll",
    }[sys.platform]

    # Get the path where the libraries are installed
    libray_path : str = os.path.join(sysconfig.get_paths()["platlib"], __package__, "lib")
    ROOT.gSystem.SetDynamicPath(libray_path + os.pathsep + ROOT.gSystem.GetDynamicPath())
    ROOT.gSystem.SetIncludePath(libray_path + os.pathsep + ROOT.gSystem.GetIncludePath())

    for lib in libs:
        if ROOT.gSystem.Load(libfmt % lib) < 0:
            print("Faild to load %s" % (libfmt % lib))
            exit(-1)
        else:
            print("Loaded %s" % lib)


    # ROOT.gEnv.SetValue("X11.UseXft", 0)

def test_calibration() -> None:
    cal = ROOT.HDTV.Calibration()
    if cal.E2Ch(2.0) != 2.0:
        print("Calibration call failed")
        exit(-2)

def test_display() -> None:
    if sys.platform == "linux":
        None # TODO: Test for env DISPLAY=:0
    try:
        viewer = ROOT.HDTV.Display.Viewer()
    except Exception as e:
        ok = False;
        print("Failed to call ROOT.HDTV.Display.View()")
        print("- - - - - - - - - - - - - - - -")
        print(e)
        print("- - - - - - - - - - - - - - - -")
    time.sleep(20)
        
def test_fit() -> None:
    None

def test_mfile() -> None:
    None

     
def main() -> None:
    #load all libraries
    load_lib(libs)

    # test the different components
    test_calibration()
    test_display()
    test_fit()
    test_mfile()
    
    # all done
    if ok:
        print("ok")
    else:
        print("Some tests failed. Plese send this output")
