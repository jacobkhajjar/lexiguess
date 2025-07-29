import json
from objects.consonants import Consonant, Action
from objects.vowels import Vowel

def guess_lexical_sets(word, phones):
    
    # loop over each phone
    for i, phone in enumerate(phones):
        
        # skip consonants
        if isinstance(phone, Vowel):
            vowel = phone
        else:
            continue

        # define previous / first
        if i == 0:
            previous = None
            first = True
        else:
            previous = phones[i - 1]
            first = False

        # define next / last
        if i < len(phones) - 1:
            next = phones[i + 1]
            last = False
        else:
            next = None
            last = True
            

        # begin logic based on CMU ARPA
        match vowel.arpa:
    
    # LOT/START/PALM - COMPLETE - can split based on MFA dict but LOT/PALM often ambiguous
            case "AA":
                if next and next.arpa == "R":
                    vowel.lexical_set = "START"
                elif last:
                    vowel.lexical_set = "PALM"
                elif not isinstance(next, Consonant):
                    vowel.lexical_set = "PALM"
                else:
                    vowel.lexical_set = check_uk_dict(word, phones, vowel, previous, next, last, first) # type: ignore
            
            # TRAP/BATH - need logic to split
            case "AE":
                vowel.lexical_set = "TRAP/BATH"

            # STRUT - COMPLETE
            case "AH":
                if vowel.is_stressed:
                    vowel.lexical_set = "STRUT"
                else:
                    vowel.lexical_set = "commA (strut)"
            
            # THOUGHT/CLOTH/NORTH/FORCE - need logic to split
            case "AO":
                vowel.lexical_set = "THOUGHT/CLOTH/NORTH/FORCE"

            # MOUTH - COMPLETE
            case "AW":
                vowel.lexical_set = "MOUTH"

            # PRICE - COMPLETE
            case "AY":
                vowel.lexical_set = "PRICE"

            # DRESS - assumes DRESS + R is always SQUARE?
            case "EH":
                if next and next.arpa == "R":
                    vowel.lexical_set = "SQUARE"
                elif vowel.is_stressed:
                    vowel.lexical_set = "DRESS"
                else:
                    vowel.lexical_set = "commA (dress)"
            
            # NURSE/LETTER - COMPLETE
            case "ER":
                if vowel.is_stressed:
                    vowel.lexical_set = "NURSE"
                else:
                    vowel.lexical_set = "lettER"

            # FACE - COMPLETE
            case "EY":
                vowel.lexical_set = "FACE"

            # KIT / NEAR - assumes NEAR is never unstressed and KIT + R is always NEAR
            case "IH":
                if vowel.is_stressed:
                    if next and next.arpa == "R":
                        vowel.lexical_set = "NEAR"
                    else:
                        vowel.lexical_set = "KIT"
                else:
                    vowel.lexical_set = "commA (kit)"

            # FLEECE / happY / commA / NEAR - assumes NEAR is never unstressed and FLEECE + R is always NEAR
            case "IY":
                if not vowel.is_stressed:
                    if first:
                        vowel.lexical_set = "commA (fleece)"
                    else:
                        vowel.lexical_set = "happY"
                elif next and next.arpa == "R":
                    vowel.lexical_set = "NEAR"
                else:
                    vowel.lexical_set = "FLEECE"
            
            # GOAT/GOAL - COMPLETE
            case "OW":
                if next and next.arpa == "L":
                    vowel.lexical_set = "GOAL (goat)"
                else:
                    vowel.lexical_set = "GOAT"

            # CHOICE - COMPLETE
            case "OY":
                vowel.lexical_set = "CHOICE"

            # FOOT/CURE - assumes FOOT + R is always CURE
            case "UH":
                if next and next.arpa == "R":
                    vowel.lexical_set = "CURE"
                elif vowel.is_stressed:
                    vowel.lexical_set = "FOOT"
                else:
                    vowel.lexical_set = "commA (foot)"

            # GOOSE/CURE - assumes GOOSE + R is always CURE
            case "UW":
                if next and next.arpa == "R":
                    vowel.lexical_set = "CURE"
                elif vowel.is_stressed:
                    vowel.lexical_set = "GOOSE"
                else:
                    vowel.lexical_set = "commA (goose)"
            
    return vowel.lexical_set

def check_uk_dict(word, phones, vowel, previous, next, last, first):
    
    # Split sets that are merged in GenAM, accessing MFA RP dictionary
    with open("dictionaries/uk.json", "r" , encoding="utf-8") as f:
        lookup = json.load(f)
        transcriptions = lookup[word]
        lexical_set = ""

        print(f"\nUK dictionary needed to split GenAm merger...")
        print(f"MFA entry found: {transcriptions}\n")
        
        match vowel.arpa:

            # Split LOT/PALM
            case "AA":
                for transcription in transcriptions:
                    if "ɒ" in transcription and "ɑ" not in transcription:
                        if lexical_set == "LOT":
                            continue
                        lexical_set += "LOT"
                    elif "ɑ" in transcription and "ɒ" not in transcription:
                        if lexical_set == "PALM":
                            continue
                        lexical_set += "PALM"
                if lexical_set == "PALM" or lexical_set == "LOT":
                    return lexical_set
                else:
                    return "ambiguous LOT or PALM"


                        
