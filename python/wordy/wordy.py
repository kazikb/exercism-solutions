# Więcej o rozpakowaniu argumentów można znaleźć:
# https://www.geeksforgeeks.org/unpacking-arguments-in-python/?ref=rp
# https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/

OPERATION_DICT = {"plus": "__add__", "minus": "__sub__", "multiplied by": "__mul__", "divided by": "__truediv__"}

def answer(question):
    # W pierwszej kolejności usuwam sufix i prefix oraz zwracam błąd jeżeli wynikowy string będzie 0.
    # Następnie sprawdzam czy pozostały ciąg znaków to liczba i jeśli tak to go zwracam.
    question = question.removeprefix("What is").removesuffix("?").strip()
    if len(question) == 0: raise ValueError("syntax error")
    if question.lstrip("-").isdigit(): return int(question)

    is_math_operation = False
    # Pętla "for" podmienia w stringu słowa z operacjami matematycznymi na wywołania metod klasy int
    # Można je wyświetlić za pomocą polecenia "print(dir(int))". Więcej informacji dostępnych jest
    # pod linkiem: https://www.tutorialsteacher.com/python/magic-methods-in-python
    for verb, math in OPERATION_DICT.items():
        if verb in question:
            is_math_operation = True
            question = question.replace(verb, math)
    if not is_math_operation: raise ValueError("unknown operation")

    question = question.split()

    # Ostatnia pętla while jest "triki" bo w pierwszej kolejności rozpakowuje listę:
    # x, math, y, *rest = question
    # Gdzie: question[0] = x; question[1] = math; question[2] = y
    # Natomiast zapis *rest -> to cała pozostała zawartość listy.
    while len(question) > 1:
        try:
            x, math, y, *rest = question
            # Następnie w tej pętli wykonywana jest operacja matematyczna:
            # [int(x).__getattribute__(math)(int(y)), *rest]
            # która opakowywana jest w listę z doklejoną pozostała zawartośćią
            # oryginalnej listy która zawarta jest w zmiennej *rest
            question = [int(x).__getattribute__(math)(int(y)), *rest]
        except:
            raise ValueError("syntax error")

    return question[0]
