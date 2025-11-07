import sys
import os
import time
import ROOT

def test_display() -> None:
    if sys.platform == "linux" and os.getenv("DISPLAY") == None:
        raise RuntimeError("DISPLAY=:0 not set")
        return
        
    print("  Testing class View")
    w = ROOT.TGWindow()
    v = ROOT.HDTV.Display.View(w, 200, 200)
    time.sleep(1)
    v = None

    print("  Testing class View1D")
    v = ROOT.HDTV.Display.View1D(w, 200, 200)
    v.Update(True)
    time.sleep(10)
    v = None

    print("  Testing class Viewer - a window should show")
    v = ROOT.HDTV.Display.Viewer()
    time.sleep(10)
