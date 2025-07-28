import json

source = "dictionaries/uk.json"
dest = "ipa.dict"

def get_ipa(source, dest):
    ipa = set()
    with open(source, "r", encoding="utf-8") as f:
        json_dict = json.load(f)
        for word, transcriptions in json_dict.items():
            for transcription in transcriptions:
                for symbol in transcription:
                        ipa.add(symbol)
    with open(dest, "w", encoding="utf-8") as f:
        for symbol in ipa:
             f.write(f"{symbol}\n")

get_ipa(source, dest)