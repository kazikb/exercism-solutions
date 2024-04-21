def translate_word(word):

    if word[0] in 'aeiou' or word.startswith('xr') or word.startswith('yt'):
        return word + 'ay'
    elif word[0:2] in {'ch' , 'st' , 'qu' , 'th' , 'rh'} and word[0:3] != 'thr':
        return word[2:] + word[0:2] + 'ay'
    elif word[0:3] in {'squ' , 'thr' , 'sch'}:
        return word[3:] + word[0:3] + 'ay'
    else:
        return word[1:] + word[0] + 'ay'

def translate(text):
    list_of_words = text.split(' ')
    translate_list_of_words = ''
    for word in list_of_words:
        translate_list_of_words += f"{(translate_word(word))} "

    return translate_list_of_words.strip()
