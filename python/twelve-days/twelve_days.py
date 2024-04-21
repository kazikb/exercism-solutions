verse = (
    "twelve Drummers Drumming, ",
    "eleven Pipers Piping, ",
    "ten Lords-a-Leaping, ",
    "nine Ladies Dancing, ",
    "eight Maids-a-Milking, ",
    "seven Swans-a-Swimming, ",
    "six Geese-a-Laying, ",
    "five Gold Rings, ",
    "four Calling Birds, ",
    "three French Hens, ",
    "two Turtle Doves, ",
    "and a Partridge in a Pear Tree."
)
days = (
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth"
)

def recite(start_verse, end_verse):
    return_verses = []

    for count in range(start_verse, end_verse + 1):
        verse_string = f"On the {days[count - 1]} day of Christmas my true love gave to me: "
        if count -1 == 0:
            verse_string +=  "a Partridge in a Pear Tree."
        else:
            verse_string += "".join(item for item in verse[-(count)::1])
        return_verses.append(verse_string)
    return return_verses
