def response(hey_bob):
    hey_bob_strip = hey_bob.strip()

    if hey_bob_strip.endswith('?') and not hey_bob_strip.isupper():
        return "Sure."
    elif hey_bob_strip.isupper() and not hey_bob_strip.endswith('?'):
        return "Whoa, chill out!"
    elif hey_bob_strip.endswith('?') and hey_bob_strip.isupper():
        return "Calm down, I know what I'm doing!"
    elif not hey_bob_strip:
        return "Fine. Be that way!"
    else:
        return "Whatever."
        