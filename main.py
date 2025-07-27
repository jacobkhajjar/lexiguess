import cmudict
from objects.consonants import classify_consonant
from objects.vowels import Vowel, vowel_list, classify_vowel

word = "enough"
cmu = cmudict.dict()


def main():
    phones = []
    lexical_sets = set()
    tokens = cmu[word]

    print(f'lexiguessing "{word}"')
    print(f"dictionary glyphs: {tokens}")

#need to add cases for homonyms and words not in dictionary and symbol not found

    for token in tokens[0]:
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

main()