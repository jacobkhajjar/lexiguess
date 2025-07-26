import cmudict
from objects.consonants import Consonant, Action, classify_consonant
from objects.vowels import Vowel, vowel_list, classify_vowel

word = "it"
cmu = cmudict.dict()


def main():
    tokens = []
    lexical_sets = set()
    phones = cmu[word]

    print(f'lexiguessing "{word}"')
    print(f"dictionary glyphs: {phones}")

#need to add cases for homonyms and words not in dictionary

    for phone in phones[1]:
        if phone[0] in vowel_list:
            token = classify_vowel(phone)
        else:
            token = classify_consonant(phone)
        
        tokens.append(token)

    transcription = ""
    for token in tokens:
        glyphs = token.glyphs
        if isinstance(token, Vowel) and not token.is_stressed:
            glyphs = glyphs.lower()
        transcription += glyphs + " "
    print(f"fauxnetic transcription: {transcription}")

main()