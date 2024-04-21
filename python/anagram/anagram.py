# https://pl.wikipedia.org/wiki/Anagram
#
# Dla tego zadania rozwiązaniem jest posortowanie każdego wyrazu alfabetycznie
# Metoda sorted zamienia string na listę znaków i sortuje ją alfabetycznie.
# W tym wypadku czy dane słowo jest anagramem to muszą się składać z tych samych liter.

def find_anagrams(word, candidates):
    word_lower = word.lower()
    word_sorted = sorted(word_lower)
    anagram_list = []
    for candidate in candidates:
        if word_sorted == sorted(candidate.lower()) and word_lower != candidate.lower():
            anagram_list.append(candidate)
    return anagram_list
