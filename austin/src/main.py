from enum import Enum
class TclOut(Enum):
    CRN = 0
    TC = 1
    PRE_BAL = 2
    DATE = 3
    TRANS = 4
    POST_BAL = 5

class FeeRep(Enum):
    CRN = 0
    PAYMENT_DATE = 1
    TRANS = 2
    ULTRA_POST_BAL = 3

tcl_file = open("../input/tcl_out.txt")
rep_file = open("../input/fee_report.txt")

print(tcl_file.read())
