import string

def rows(letter):
    alphabet = list(string.ascii_uppercase)
    number_of_letters = alphabet.index(letter.upper())
    image = []

    for print_letter in range(0,number_of_letters + 1):
        letter_index = alphabet.index(alphabet[print_letter])

        line = " " * (number_of_letters - letter_index) + alphabet[print_letter]
        if alphabet[print_letter] != "A": line += " " * (letter_index * 2 - 1) + alphabet[print_letter]
        line += " " * (number_of_letters - letter_index)

        image.append(line)

    image_reverse = image[:-1]
    if image_reverse:
        image_reverse.reverse()
        return image + image_reverse
    else:
        return image
