import random

class Die:
  def __init__(self, sides: int):
    self.sides = sides

  def roll(self, times = 1):
    total = []

    for i in range(0,times):
      total.append(random.randint(1, self.sides))
    return total