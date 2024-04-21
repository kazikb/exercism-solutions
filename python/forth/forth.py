class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message

def arithmetic_operation(input, stack) -> []:
    """
    Funkcja przeprowadzająca operacje arytmetyczne na 2 ostatnich elementach
    znajdujących się na stosie.

    :param input: str - operacja jaka ma być wykonana na stosie.
    :param stack: [] - aktualny stan stosu (zawiera liczby na jakich ma być
                        przeprowadzona operacja).
    :return stack: [] - zwraca stan stosu po modyfikacji.
    """
    if len(stack) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")
    x = stack.pop(-2)
    y = stack.pop()
    if input == "+":
        stack.append(x + y)
    elif input == "-":
        stack.append(x - y)
    elif input == "*":
        stack.append(x * y)
    elif input == "/":
        if y <= 0:
            raise ZeroDivisionError("divide by zero")
        stack.append(int(x / y))
    return stack

def stack_manipulation(input, stack) -> []:
    """
    Funkcja przeprowadzająca operacje na stosie: DUP/DROP/SWAP/OVER.
    Dla DUP i DROP wymaga co najmniej 1 wartości umieszczonej na stosie.
    Dla SWAP i OVER wymaga co najmniej 2 wartości umieszczonej na stosie.
    DUP - zduplikowanie ostatniego elementu na stosie.
    DROP - usunięcie ostatniego elementu ze stosu.
    SWAP - zamiana przed ostatniego z ostatnim elementem na stosie.
    OVER - dodanie na końcu stosu zduplikowanego przedostatniego elementu.

    :param input: str - operacja jaka ma być wykonana na stosie.
    :param stack: [] - aktualny stan stosu (zawiera liczby na jakich ma być
                        przeprowadzona operacja).
    :return stack: [] - zwraca stan stosu po modyfikacji.
    """
    if len(stack) < 1:
        raise StackUnderflowError("Insufficient number of items in stack")
    if input.upper() == "DUP":
        stack.append(stack[-1])
    elif input.upper() == "DROP":
        stack.pop()
    elif input.upper() == "SWAP":
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack")
        x = stack.pop(-2)
        y = stack.pop()
        stack.append(y)
        stack.append(x)
    elif input.upper() == "OVER":
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack")
        stack.append(stack[-2])
    return stack

def evaluate(input_data):
    stack = []
    command = {}

    while input_data:
        input = input_data.pop(0)

        # Warunek sprawdzający czy aktualny ciąg parametrów jest
        # typu word-name czy danymi na których mają być przeprowadzone
        # operacje na stosie.
        if input.startswith(":"):
            # W przypadku word-name usuwamy unikatowe znaki które go definiują
            # Następnie pierwszy element jest unikatową nazwą word-name i będzie
            # tworzyć pole key w obiekcie dict. Pole value będzie zawierać pozostałe
            # elementy które definiują operacje do przeprowadzenia. Mogą to być
            # inne word-name dlatego w pętli for sprawdzamy czy taki word-name
            # już znajduje się w dict->command i jeśli tak to podmieniamy dany wyraz
            # na zapisany w danym kluczu ciąg operacji.
            input = input.lstrip(": ").rstrip(" ;").split(" ")
            # Sprawdzamy czy word-name nie składa się z samych cyfr.
            if all([item.lstrip("-").isdigit() for item in input]):
                raise ValueError("illegal operation")
            key = input[0].lower()
            value = input[1:]
            value_stack = value.copy()
            for record in value_stack:
                if record in command:
                    for i in command[record]:
                        value.insert(value.index(record), i)
                    value.remove(record)
            command[key] = value
            continue
        else:
            # W przypadku kiedy mamy rekord zawierający listę operacji
            # do wykonania i tak musimy sprawdzić czy nie znajduje się w nim jakiś
            # word-name. Jeśli pole key obiektu dict->command odpowiada jakiejś wartości
            # z listy input to w jego miejsce wstawiamy powiązane z tym kluczem wartości
            # value.
            input = input.split(" ")
            input_stack = input.copy()
            for record in input_stack:
                key = record.lower()
                if key in command:
                    for i in command[key]:
                        input.insert(input.index(record), i)
                    input.remove(record)

        for item in input:
            if item.lstrip("-").isdigit():
                stack.append(int(item))
            elif item in "+-*/":
                stack = arithmetic_operation(item, stack)
            elif item.upper() in ("DUP", "DROP", "SWAP", "OVER"):
                stack = stack_manipulation(item, stack)
            else:
                raise ValueError("undefined operation")
    return(stack)
