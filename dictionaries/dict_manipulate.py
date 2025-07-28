# run this file if you would like to find/replace in one of the "pretty" dictionaries. Run update_dict after to ensure the changes are applied to the json files for use in other functions.

f_or_r = input("Find or replace? (f or r): ").lower()

response = input('Which dictionary would you like to update?\n(Enter "US" or "UK"): ').lower()

if response == "us":
    source = "dictionaries/pretty/us.dict"
elif response == "uk":
    source = "dictionaries/pretty/uk.dict"
else:
    raise ValueError('Invalid input. Valid options are "US" or "UK"')

search = input("Search for: ")

if f_or_r == "r":
    replacement = input(f"Replace {search} with: ")

def dict_find():
    found = []
    with open(source, "r", encoding="utf-8") as f:
        for line in f:
            if search in line:
                found.append(line)
    with open("dict_find_results.txt", "w", encoding="utf-8") as f:
        for item in found:
            f.write(item)

def dict_replace():
    with open(source, "r", encoding="utf-8") as f:
        with open("dict_replace_results.txt", "w", encoding="utf-8") as g:
            for line in f:
                new_line = line.replace(search, replacement)
                g.write(new_line)

if f_or_r == "f":
    print(f"Finding {search} in {source}...")
    dict_find()

if f_or_r == "r":
    print(f"Replacing {search} with {replacement} in {source}...")
    dict_replace()

print("Dictionary manipulation complete!")