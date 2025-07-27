from enum import Enum
from objects.phones import Phone
from config.fauxnetics import *

class Action(Enum):
    STOP = 1
    FRICATIVE = 2
    NASAL = 3
    AFFRICATE = 4
    LIQUID = 5
    SEMIVOWEL = 6

class Consonant(Phone):
    def __init__(self, fx: str, is_voiced: bool, action: Action):
        super().__init__(fx)
        self.is_voiced = is_voiced
        self.action = action

def classify_consonant(token):
    match token:

        case "B":
            consonant = Consonant(fx_B, True, Action.STOP)
        case "CH":
            consonant = Consonant(fx_CH, False, Action.AFFRICATE)
        case "D":
            consonant = Consonant(fx_D, True, Action.STOP)
        case "DH":
            consonant = Consonant(fx_DH, True, Action.FRICATIVE)
        case "F":
            consonant = Consonant(fx_F, False, Action.FRICATIVE)
        case "G":
            consonant = Consonant(fx_G, True, Action.STOP)
        case "HH":
            consonant = Consonant(fx_HH, False, Action.FRICATIVE)
        case "JH":
            consonant = Consonant(fx_JH, True, Action.AFFRICATE)
        case "K":
            consonant = Consonant(fx_K, False, Action.STOP)
        case "L":
            consonant = Consonant(fx_L, True, Action.LIQUID)
        case "M":
            consonant = Consonant(fx_M, True, Action.NASAL)
        case "N":
            consonant = Consonant(fx_N, True, Action.NASAL)
        case "NG":
            consonant = Consonant(fx_NG, True, Action.NASAL)
        case "P":
            consonant = Consonant(fx_P, False, Action.STOP)
        case "R":
            consonant = Consonant(fx_R, True, Action.LIQUID)
        case "S":
            consonant = Consonant(fx_S, False, Action.FRICATIVE)
        case "SH":
            consonant = Consonant(fx_SH, False, Action.FRICATIVE)
        case "T":
            consonant = Consonant(fx_T, False, Action.STOP)
        case "TH":
            consonant = Consonant(fx_TH, False, Action.FRICATIVE)
        case "V":
            consonant = Consonant(fx_V, True, Action.FRICATIVE)
        case "W":
            consonant = Consonant(fx_W, True, Action.SEMIVOWEL)
        case "Y":
            consonant = Consonant(fx_Y, True, Action.SEMIVOWEL)
        case "Z":
            consonant = Consonant(fx_Z, True, Action.FRICATIVE)
        case "ZH":
            consonant = Consonant(fx_ZH, True, Action.FRICATIVE)
   
    return consonant
