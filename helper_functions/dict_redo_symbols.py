mapping = {
  "vowels": {
    "IY": ["i", "i"],
    "IH": ["ɪ", "ɪ"],
    "EY": ["eɪ", "eɪ"],
    "EH": ["ɛ", "ɛ"],
    "AE": ["æ", "a"],
    "AA": ["ɑ", "ɑ"],
    "AO": ["ɔ", "ɔ"],
    "OW": ["oʊ", "əʊ"],
    "UH": ["ʊ", "ʊ"],
    "UW": ["u", "u"],
    "AH": ["ʌ", "ʌ"],
    "ER": ["ɝ", "ɜ"],
    "AX": ["ə", "ə"],
    "AXR": ["ɚ", "ə"],
    "AY": ["aɪ", "aɪ"],
    "AW": ["aʊ", "aʊ"],
    "OY": ["ɔɪ", "ɔɪ"],
    "OX": ["ɑ", "ɒ"]
  },
  "consonants": {
    "P": ["p", "p"],
    "B": ["b", "b"],
    "T": ["t", "t"],
    "D": ["d", "d"],
    "K": ["k", "k"],
    "G": ["ɡ", "ɡ"],
    "CH": ["tʃ", "tʃ"],
    "JH": ["dʒ", "dʒ"],
    "F": ["f", "f"],
    "V": ["v", "v"],
    "TH": ["θ", "θ"],
    "DH": ["ð", "ð"],
    "S": ["s", "s"],
    "Z": ["z", "z"],
    "SH": ["ʃ", "ʃ"],
    "ZH": ["ʒ", "ʒ"],
    "HH": ["h", "h"],
    "M": ["m", "m"],
    "N": ["n", "n"],
    "NG": ["ŋ", "ŋ"],
    "L": ["l", "l"],
    "R": ["ɹ", "ɹ"],
    "Y": ["j", "j"],
    "W": ["w", "w"]
  }
}

filtered_phonemes = [
    "ej", "bʲ",
    "dʲ", "ç", "ɟ", "tʲ", "mʲ"
]

def redo_liquid_u():
    replacements = {
        "tʲ": "t",
        "dʲ": "d",
        "bʲ": "b",
        "pʲ": "p",
        "mʲ": "m",
        "fʲ": "f",
        "ç": "h",
        "ɟ": "ɡ",
        "vʲ": "v"
    }

    with open("new_dict.txt", "w", encoding="utf-8") as f:
        with open("dictionaries/pretty/uk.dict", "r", encoding="utf-8") as g:
            for line in g:
                line_list = line.strip().split()
                ipa_list = line_list[1:]  # everything after the word
                new_ipa_list = []
                i = 0
                while i < len(ipa_list):
                    symbol = ipa_list[i]
                    if symbol in replacements:
                        base = replacements[symbol]
                        if i + 1 < len(ipa_list) and ipa_list[i + 1] == "u":
                            new_ipa_list.append(base)
                            new_ipa_list.append("j")
                        else:
                            new_ipa_list.append(base)
                        i += 1
                    else:
                        new_ipa_list.append(symbol)
                        i += 1
                new_line = f"{line_list[0]} {' '.join(new_ipa_list)}\n"
                f.write(new_line)

redo_liquid_u()