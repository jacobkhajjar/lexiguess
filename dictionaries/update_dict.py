# run this file if you have edited a "pretty" dictionary and would like to apply these updates to the JSON file for use in other functions

import json

def main():
    response = input('Which dictionary would you like to update?\n(Enter "US" or "UK"): ').lower()
    if response == "us":
        old_dict = "dictionaries/pretty/us.dict"
        dest = "dictionaries/us.json"
    elif response == "uk":
        old_dict = "dictionaries/pretty/uk.dict"
        dest = "dictionaries/uk.json"
    else:
        raise ValueError('Invalid input. Valid options are "US" or "UK"')
    
    new_dict = dict_convert(old_dict)

    update_dict(new_dict, dest)

def dict_convert(old_dict):
    new_dict = {}
    with open(old_dict) as f:
        for line in f:
            transcription = line.split()
            word = transcription[0]
            if word in new_dict:
                new_dict[word].append(transcription[1:])
            else:
                new_dict[word] = [transcription[1:]]
    return new_dict

def update_dict(new_dict, dest):
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(new_dict, f, ensure_ascii=False)

main()