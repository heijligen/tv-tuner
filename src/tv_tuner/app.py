
import sysconfig
from pathlib import Path
import os
import sys

import ROOT

libfmt = {
    "linux" : "lib%s.so",
    "darwin": "lib%s.dylib",
    "win32" :    "%s.dll",
}[sys.platform]

def main() -> None:

    libs = ["calibration"]
    
    libray_path : str = os.path.join(sysconfig.get_paths()["platlib"], __package__, "lib")
    ROOT.gSystem.SetDynamicPath(libray_path + os.pathsep + ROOT.gSystem.GetDynamicPath())
    ROOT.gSystem.SetIncludePath(libray_path + os.pathsep + ROOT.gSystem.GetIncludePath())

    for lib in libs:
        if ROOT.gSystem.Load(libfmt % lib) < 0:
            print("Faild to load %s" % (libfmt % lib))
            exit(-1)
        else:
            print("Loaded %s" % lib)
        
    cal = ROOT.HDTV.Calibration()
    print(cal.E2Ch(2.0))
