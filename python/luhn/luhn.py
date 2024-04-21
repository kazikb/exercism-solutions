class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ","")

    def valid(self):
        if not self.card_num.isdigit() or len(self.card_num) <= 1:
            return False

        card_number_sum = 0

        # Można to rozwiązać na dwa sposoby:

        # for number in self.card_num[-2::-2]:
        #     number = int(number) * 2
        #     card_number_sum += number - 9 if number >= 9 else number
        # card_number_sum += sum(int(number) for number in self.card_num[::-2])

        for index, number in enumerate(self.card_num[::-1]):
            number = int(number)
            if index % 2 == 0:
                card_number_sum += number
            else:
                number = number * 2
                card_number_sum += number -9 if number >= 9 else number

        return card_number_sum % 10 == 0
