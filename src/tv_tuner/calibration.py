
import ROOT

def test_calibration() -> None:
    print("  Testing class Calibraiton")
    cal = ROOT.HDTV.Calibration()
    cal1 = ROOT.HDTV.Calibration(1.0)
    cal2 = ROOT.HDTV.Calibration(2.0, 3)
    cal.SetCal(42.73)
    print("  "
        + str(cal1.Ch2E(5.2)) + " "
        + str(cal2.dEdCh(5.2)) + " "
        + str(cal.E2Ch(5.2)))
