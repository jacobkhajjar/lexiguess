import json

with open("dictionaries/pretty/us.dict", "w") as new_file:
    with open("dictionaries/us.json", "r" , encoding="utf-8") as f:
        json_dict = json.load(f)
        for word, transcriptions in json_dict.items():
            for transcription in transcriptions:
                new_file.write(f"{word} {' '.join(transcription)}\n")