import argparse
import json

from objects.consonants import classify_consonant
from objects.vowels import Vowel, vowel_list, classify_vowel
from guess_lexical_sets import guess_lexical_sets

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
parser.add_argument('-fx', '--fauxnetics', action='store_true', help='Enable fauxnetic transcription')
args = parser.parse_args()

verbose = args.verbose
do_fx = args.fauxnetics

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
        if verbose:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f'\nLexiguessing "{word}" ({i + 1} of {word_count}):\n')
        
        # check if word is in dict
        try:
            tokens = lookup[word]
        except:
            print(f'"{word}" not in CMU dictionary\n')
            i += 1
            continue

        # loop for each homonym found in dict
        homonyms = 0
        while homonyms < len(tokens):
            if verbose:
                print(f"CMU entry found: {tokens[homonyms]}\n")
            
            # convert dict tokens into Phone objects
            phones = []
            for token in tokens[homonyms]:
                if token[0] in vowel_list:
                    new_phone = classify_vowel(token)
                else:
                    new_phone = classify_consonant(token)
                phones.append(new_phone)

            # guess lexical sets
            guess_lexical_sets(word, phones, verbose)
            
            lexical_sets = []
            transcription = ""
            
            # loop through each phone for final analysis
            for phone in phones:

                # build lexical set list
                if isinstance(phone, Vowel) and phone.lexical_set not in lexical_sets:
                    lexical_sets.append(phone.lexical_set)

                # build fauxnetic transcription if -fx
                if do_fx:
                    fauxnetic = phone.fx
                    if isinstance(phone, Vowel) and not phone.is_stressed:
                        fauxnetic = fauxnetic.lower() # unstressed vowels to lowercase
                    transcription += fauxnetic + "."
            
            
            # print results
            if verbose:
                print(f"Best guess at lexical sets: {", ".join(lexical_sets)}\n")
            else:
                print(f"{word}: {", ".join(lexical_sets)}")
            if do_fx:
                print(f"fauxnetic transcription (GenAm): {transcription.strip(".")}")
            
            # check for homonyms
            if homonyms != len(tokens) - 1:
                if verbose:
                    print("\n~~~ homonym found, running again ~~~\n")
            homonyms += 1
        
        # increment to check for next word
        i += 1
    
    # footer
    if verbose:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\nLexiguess complete!\n")
    
    return

main()