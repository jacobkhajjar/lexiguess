source = "english_uk_mfa.dict"
dest = "uk_dict_text.dict"

def dict_remove_numbers(source, dest):
    with open(dest, "w") as f:
        with open(source) as g:
            for line in g:
                raw = line.split()
                word = raw[0]
                ipa = []
                for item in raw[1:]:
                    try:
                        float(item)
                    except ValueError:
                        ipa.append(item)
                f.write(f"{word} {" ".join(ipa)}\n")

dict_remove_numbers(source, dest)