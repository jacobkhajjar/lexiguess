import cmudict
from objects.consonants import classify_consonant
from objects.vowels import Vowel, vowel_list, classify_vowel




def main():
    entry = input("What word would you like to lexiguess?: ")
    entry = entry.split()

    word_count = len(entry)
    i = 0
    
    cmu = cmudict.dict()

    while i < word_count:
        word = entry[i]
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f'\nLexiguessing "{word}" ({i + 1} of {word_count}):\n')
        
        try:
            tokens = cmu[word]
        except:
            print(f'"{word}" not in CMU dictionary')
            continue

        homonyms = 0

        while homonyms < len(tokens):
            print(f"CMU entry found: {tokens[homonyms]}\n")
            
            phones = []

            for token in tokens[homonyms]:
                if token[0] in vowel_list:
                    new_phone = classify_vowel(token)
                else:
                    new_phone = classify_consonant(token)
            
                phones.append(new_phone)

            transcription = ""
            for phone in phones:
                fauxnetic = phone.fx
                if isinstance(phone, Vowel) and not phone.is_stressed:
                    fauxnetic = fauxnetic.lower()
                transcription += fauxnetic + " "
                
            print(f"fauxnetic transcription: {transcription}\n")
            
            if homonyms != len(tokens) - 1:
                print("\n~~~ homonym found, running again ~~~\n")

            homonyms += 1
        
        i += 1
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n Lexiguess complete!\n")
    return

main()