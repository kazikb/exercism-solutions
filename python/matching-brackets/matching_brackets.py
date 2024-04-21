# Rozwiązanie tego zadania należy oprzeć o pojęcie stosu
# czyli kolejki LIFO (Last In First Out). Jeżeli natrafimy
# na otwierający nawias dodajemy go na stos. Jeżeli
# natrafimy na zamykający nawias a na stosie nie ma odpowiadającego
# mu nawiasu otwierającego to kończymy sprawdzanie i zwracamy False.
# Jeżeli jest na stosie odpowiadający mu nawias otwierajacy to usuwamy
# go ze stosu (jako zamknięta para).
# Ostatni fragment "return not stack" zwraca True jeżeli lista jest pusta.

def is_paired(input_string):
    pairs_open = ["(", "[", "{"]
    pairs_close = [")", "]", "}"]
    stack = []

    for item in input_string:
        if item in pairs_open: stack.append(item)
        elif item in pairs_close:
            if not stack or pairs_open[pairs_close.index(item)] != stack.pop():
                return False
    return not stack
