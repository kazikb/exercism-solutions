def is_armstrong_number(number):
    number_str = str(number)
    total = 0

    for i in number_str:
        total += int(i) ** len(number_str)

    return number == total
    