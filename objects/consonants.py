from enum import Enum
from objects.phones import Phone
import config.fauxnetics

class Action(Enum):
    STOP = 1
    FRICATIVE = 2
    NASAL = 3
    AFFRICATE = 4
    LIQUID = 5
    SEMIVOWEL = 6

class Consonant(Phone):
    def __init__(self, glyphs: str, is_voiced: bool, action: Action):
        super().__init__(glyphs)
        self.is_voiced = is_voiced
        self.action = action

def classify_consonant(phone):
    match phone:

        case "B":
            consonant = Consonant(fx_B, True, Action.STOP)
        case "CH":
            consonant = Consonant(fx_CH, False, Action.AFFRICATE)
        case "D":
            consonant = Consonant("d", True, Action.STOP)
        case "DH":
            consonant = Consonant("th(v)", True, Action.FRICATIVE)
        case "F":
            consonant = Consonant("f", False, Action.FRICATIVE)
        case "G":
            consonant = Consonant("g", True, Action.STOP)
        case "HH":
            consonant = Consonant("h", False, Action.FRICATIVE)
        case "JH":
            consonant = Consonant("j", True, Action.AFFRICATE)
        case "K":
            consonant = Consonant("k", False, Action.STOP)
        case "L":
            consonant = Consonant("l", True, Action.LIQUID)
        case "M":
            consonant = Consonant("m", True, Action.NASAL)
        case "N":
            consonant = Consonant("n", True, Action.NASAL)
        case "NG":
            consonant = Consonant("ng", True, Action.NASAL)
        case "P":
            consonant = Consonant("p", False, Action.STOP)
        case "R":
            consonant = Consonant("r", True, Action.LIQUID)
        case "S":
            consonant = Consonant("s", False, Action.FRICATIVE)
        case "SH":
            consonant = Consonant("sh", False, Action.FRICATIVE)
        case "T":
            consonant = Consonant("t", False, Action.STOP)
        case "TH":
            consonant = Consonant("th(uv)", False, Action.FRICATIVE)
        case "V":
            consonant = Consonant("v", True, Action.FRICATIVE)
        case "W":
            consonant = Consonant("w", True, Action.SEMIVOWEL)
        case "Y":
            consonant = Consonant("y", True, Action.SEMIVOWEL)
        case "Z":
            consonant = Consonant("z", True, Action.FRICATIVE)
        case "ZH":
            consonant = Consonant("zh", True, Action.FRICATIVE)
   
    return consonant
