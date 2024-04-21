ANIMAL_LIST = (
    "fly",
    "spider",
    "bird",
    "cat",
    "dog",
    "goat",
    "cow",
    "horse"
)
UNIQUE_SENTENCES = {
    "spider": "It wriggled and jiggled and tickled inside her.",
    "bird": "How absurd to swallow a bird!",
    "cat": "Imagine that, to swallow a cat!",
    "dog": "What a hog, to swallow a dog!",
    "goat": "Just opened her throat and swallowed a goat!",
    "cow": "I don't know how she swallowed a cow!"
}


def recite(start_verse, end_verse):
    lyrics = []

    for item in range(start_verse - 1, end_verse):
        lyrics.append(f"I know an old lady who swallowed a {ANIMAL_LIST[item]}.")

        if ANIMAL_LIST[item] == "horse":
            lyrics.append("She's dead, of course!")
        else:
            if UNIQUE_SENTENCES.get(ANIMAL_LIST[item], False):
                lyrics.append(UNIQUE_SENTENCES[ANIMAL_LIST[item]])

            if item >= 1:
                i = item
                while i > 0:
                    lyrics.append(f"She swallowed the {ANIMAL_LIST[i]} to catch the {ANIMAL_LIST[i-1]}")
                    if ANIMAL_LIST[i-1] == "spider":
                        lyrics[-1] += " that wriggled and jiggled and tickled inside her."
                    else:
                        lyrics[-1] += "."
                    i -= 1

            lyrics.append("I don't know why she swallowed the fly. Perhaps she'll die.")

        if item + 1 < end_verse:
            lyrics.append("")

    return lyrics
