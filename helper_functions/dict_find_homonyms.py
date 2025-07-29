import json

source = "dictionaries/uk.json"
dest = "dict_homonym_results.txt"

def dict_find_homonyms():
    homonyms = {}
    with open(source, "r" , encoding="utf-8") as f:
        json_dict = json.load(f)
        for word, transcriptions in json_dict.items():
            if len(transcriptions) > 1:
                homonyms[word] = transcriptions

    with open(dest, "w" , encoding="utf-8") as f:
        for word, transcriptions in homonyms.items():
            for transcription in transcriptions:
                f.write(f"{word} {transcription}\n")

dict_find_homonyms()