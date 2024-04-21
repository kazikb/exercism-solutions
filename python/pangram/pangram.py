# Importowanie wszystkich znaków ASCII
from string import ascii_lowercase

def is_pangram(sentence):
    """
    Function to check if sentence is pangram.

    :param sentence: str - sentence to check
    :return: bool
    """
    sentence = sentence.lower()

    for letter in ascii_lowercase:
        if letter not in sentence:
            return False
    return True
