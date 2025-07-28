mapping = {
  "vowels": {
    "IY": ["i"],
    "IH": ["ɪ"],
    "EY": ["eɪ"],
    "EH": ["ɛ"],
    "AE": ["æ", "a"],
    "AA": ["ɑ"],
    "AO": ["ɔ"],
    "OW": ["oʊ", "əʊ"],
    "UH": ["ʊ"],
    "UW": ["u"],
    "AH": ["ʌ"],
    "ER": ["ɝ", "ɜ"],
    "AX": ["ə"],
    "AXR": ["ɚ"],
    "AY": ["aɪ"],
    "AW": ["aʊ"],
    "OY": ["ɔɪ"],
    "OX": ["ɒ"]
  },
  "consonants": {
    "P": ["p"],
    "B": ["b"],
    "T": ["t"],
    "D": ["d"],
    "K": ["k"],
    "G": ["ɡ"],
    "CH": ["tʃ"],
    "JH": ["dʒ"],
    "F": ["f"],
    "V": ["v"],
    "TH": ["θ"],
    "DH": ["ð"],
    "S": ["s"],
    "Z": ["z"],
    "SH": ["ʃ"],
    "ZH": ["ʒ"],
    "HH": ["h"],
    "M": ["m"],
    "N": ["n"],
    "NG": ["ŋ"],
    "L": ["l"],
    "R": ["ɹ"],
    "Y": ["j"],
    "W": ["w"]
  }
}

filtered_ipa_symbols = [
    "tʲ", "ç", "fʲ",
    "bʲ", "pʲ",
    "dʲ"
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