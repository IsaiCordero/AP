from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

class Node:
    def __init__(self, index, taken, value, room):
        self.index = index
        self.taken = taken
        self.value = value
        self.room = room
        return

    def estimate(self, items):
        valor = self.value
        for i in range(self.index, len(items)):
            valor += items[i].value
        return valor
