# https://docs.python.org/3/library/re.html#re.findall

import re

def count_words(sentence):
    word_count = re.findall(r"[a-z\d]+'?[a-z\d]+|\d+|[a-z\d]+", sentence.lower())
    return {word: word_count.count(word) for word in word_count}
