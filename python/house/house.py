NURSERY_RHYME = (
    "the house that Jack built.",
    "the malt that lay in",
    "the rat that ate",
    "the cat that killed",
    "the dog that worried",
    "the cow with the crumpled horn that tossed",
    "the maiden all forlorn that milked",
    "the man all tattered and torn that kissed",
    "the priest all shaven and shorn that married",
    "the rooster that crowed in the morn that woke",
    "the farmer sowing his corn that kept",
    "the horse and the hound and the horn that belonged to"
)

def recite(start_verse, end_verse) -> list:
    """Function implementing recite the nursery rhyme."""

    verse_num = end_verse - start_verse + 1
    result = []
    for n in range(verse_num):
        verse_rhyme_len = start_verse + n
        verse = ["This is"]
        for i in range(verse_rhyme_len, 0, -1):
            verse.append(NURSERY_RHYME[i-1])
        result.append(" ".join(verse))
    return result
