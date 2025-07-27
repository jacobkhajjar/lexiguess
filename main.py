import cmudict
from objects.consonants import classify_consonant
from objects.vowels import Vowel, vowel_list, classify_vowel

word = "object"
cmu = cmudict.dict()


def main():
    lexical_sets = set()
    tokens = cmu[word]
    i = 0

    print(f'lexiguessing "{word}"\n')

#need to add cases for words not in dictionary and symbol not found

    while i < len(tokens):
        print(f"dictionary glyphs: {tokens[i]}")
        
        phones = []

        for token in tokens[i]:
            if token[0] in vowel_list:
                token = classify_vowel(token)
            else:
                token = classify_consonant(token)
        
            phones.append(token)

        transcription = ""
        for phone in phones:
            fauxnetic = phone.fx
            if isinstance(phone, Vowel) and not phone.is_stressed:
                fauxnetic = fauxnetic.lower()
            transcription += fauxnetic + " "
        print(f"fauxnetic transcription: {transcription}")
        
        if i != len(tokens) - 1:
            print("\n~~~ homonym found, running again ~~~\n")

        i += 1

main()