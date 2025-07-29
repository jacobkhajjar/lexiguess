import json

from objects.consonants import classify_consonant
from objects.vowels import Vowel, vowel_list, classify_vowel
from guess_lexical_sets import guess_lexical_sets

def main():
    # user entry
    entry = input("What word would you like to lexiguess?: ").lower()
    entry = entry.split()

    # define counters
    word_count = len(entry)
    i = 0
    
    # define dict
    with open("dictionaries/us.json", "r" , encoding="utf-8") as f:
        lookup = json.load(f)

    # loop for each word in entry
    while i < word_count:
        word = entry[i]
        
        # header
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f'\nLexiguessing "{word}" ({i + 1} of {word_count}):\n')
        
        # check if word is in dict
        try:
            tokens = lookup[word]
        except:
            print(f'"{word}" not in CMU dictionary')
            i += 1
            continue

        # loop for each homonym found in dict
        homonyms = 0
        while homonyms < len(tokens):
            print(f"CMU entry found: {tokens[homonyms]}")
            
            # convert dict tokens into Phone objects
            phones = []
            for token in tokens[homonyms]:
                if token[0] in vowel_list:
                    new_phone = classify_vowel(token)
                else:
                    new_phone = classify_consonant(token)
                phones.append(new_phone)

            # guess lexical sets
            guess_lexical_sets(word, phones)
            
            lexical_sets = []
            transcription = ""
            
            # loop through each phone for final analysis
            for phone in phones:

                # build lexical set list
                if isinstance(phone, Vowel) and phone.lexical_set not in lexical_sets:
                    lexical_sets.append(phone.lexical_set)

                # build fauxnetic transcription
                fauxnetic = phone.fx
                if isinstance(phone, Vowel) and not phone.is_stressed:
                    fauxnetic = fauxnetic.lower() # unstressed vowels to lowercase
                transcription += fauxnetic + "."
            
            # print phone iteration results
            print(f"fauxnetic transcription (GenAm): {transcription.strip(".")}")
            print(f"Best guess at lexical sets: {", ".join(lexical_sets)}\n")
            
            # check for homonyms
            if homonyms != len(tokens) - 1:
                print("\n~~~ homonym found, running again ~~~\n")
            homonyms += 1
        
        # increment to check for next word
        i += 1
    
    # footer
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nLexiguess complete!\n")
    
    return

main()