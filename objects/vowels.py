from objects.phones import Phone
from config.fauxnetics import *

vowel_list = ["A", "E", "I", "O", "U"]

class Vowel(Phone):
    def __init__(self, fx: str, is_stressed = True):
         super().__init__(fx)
         self.is_stressed = is_stressed
         self.possible_sets = set()

    def __repr__(self):
        if not self.is_stressed:
            return self.fx.lower()
        return self.fx

def classify_vowel(token):
    match token[:2]:
        case "AA":
            vowel = Vowel(fx_AA)
        case "AE":
            vowel = Vowel(fx_AE)
        case "AH":
            vowel = Vowel(fx_AH)
        case "AO":
            vowel = Vowel(fx_AO)
        case "AW":
            vowel = Vowel(fx_AW)
        case "AY":
            vowel = Vowel(fx_AY)
        case "EH":
            vowel = Vowel(fx_EH)
        case "ER":
            vowel = Vowel(fx_ER)
        case "EY":
            vowel = Vowel(fx_EY)
        case "IH":
            vowel = Vowel(fx_IH)
        case "IY":
            vowel = Vowel(fx_IY)
        case "OW":
            vowel = Vowel(fx_OW)
        case "OY":
            vowel = Vowel(fx_OY)
        case "UH":
            vowel = Vowel(fx_UH)
        case "UW":
            vowel = Vowel(fx_UW)
        case _:
            return 1
    
    if "0" in token:
        vowel.is_stressed = False

    return vowel