from random import randint

class Die:
    def __init__(self, sides= 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))
    
if __name__ == '__main__':
    dado = Die()
    dado.roll_die()

    for i in range(20):
        dado.roll_die()

    dado2 = Die(10)

    for v in range(10):
        dado2.roll_die()