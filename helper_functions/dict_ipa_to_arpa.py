import json

source = "dictionaries/pretty/uk.ipa"
dest = "uk.dict"

with open("symbols.json", "r", encoding="utf-8") as f:
    symbols = json.load(f)

ipa_to_arpa = {}
for cat in symbols.values():
    for arpa, ipa_pair in cat.items():
        ipa = ipa_pair[1]
        ipa_to_arpa[ipa] = arpa

def dict_ipa_to_arpa():
    with open(source, "r" , encoding="utf-8") as f, open(dest, "w" , encoding="utf-8") as g:
            for line in f:
                parts = line.strip().split()
                new_line = [parts[0]]
                for phone in parts[1:]:
                    arpa = ipa_to_arpa.get(phone)
                    if arpa:
                        new_line.append(arpa)
                    else:
                        raise KeyError(f"symbol {phone} not in symbols dictionary")
                g.write(" ".join(new_line) + "\n")

dict_ipa_to_arpa()