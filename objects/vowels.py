from objects.phones import Phone
import config.fauxnetics

vowel_list = ["A", "E", "I", "O", "U"]

class Vowel(Phone):
    def __init__(self, glyphs: str, is_stressed = True):
         super().__init__(glyphs)
         self.is_stressed = is_stressed
         self.possible_sets = set()


    def __repr__(self):
        if not self.is_stressed:
            return self.glyphs.lower()
        return self.glyphs

def classify_vowel(phone):
    match phone:
        case __:
            vowel = Vowel("")
    
    if "0" in phone:
        vowel.is_stressed = False

    return vowel




# AA LOT O
# AE TRAP A
# AH STRUT UH
# AO THOUGHT/CLOTH/NORTH/FORCE AW / OR
# AW MOUTH OW
# AY HIDE AI

# EH DRESS EH
# ER NURSE / lettER ER
# EY FACE EY

# IH KIT IH 
# IY FLEECE EE

# OW GOAT OH
# OY CHOICE OI

# UH FOOT U
# UW GOOSE OO