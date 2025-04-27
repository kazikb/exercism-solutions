import itertools
import re

def word_value(word, letter_digit):
    value = 0
    for letter in word:
        value = value * 10 + letter_digit[letter]
    return value

def solve(puzzle):
    words = re.findall(r'\b[A-Z]+\b', puzzle.upper())

    unique_letters = []
    seen = set()
    for word in words:
        for letter in word:
            if letter not in seen:
                seen.add(letter)
                unique_letters.append(letter)

    if len(unique_letters) > 10:
        raise ValueError("max number of unique letters allowed is 10")

    left_words, right_word = puzzle.replace('==', '=').split('=')
    left_words = [w.strip() for w in left_words.strip().split('+')]
    right_word = right_word.strip()

    for perm in itertools.permutations(range(10), len(unique_letters)):
        letter_digit = dict(zip(unique_letters, perm))

        if any(letter_digit[word[0]] == 0 for word in words):
            continue

        left_val = sum(word_value(word, letter_digit) for word in left_words)
        right_val = word_value(right_word, letter_digit)

        if left_val == right_val:
            return letter_digit

    return None
