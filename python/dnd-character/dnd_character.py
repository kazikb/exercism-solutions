from random import randrange

def modifier(num):
    return (num - 10) // 2
    
class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        trow_list = [randrange(1,6) for i in range(4)]
        return sum(sorted(trow_list, reverse=True)[:3])
