# 1. Copia aqui tu solución del primer ejercicio de esta semana

def next_number(digits, base):
    """
    :param digits: list containing all the digits of a number
                   in the given base
    :param base: numeric base of the number
    :return: list representing the next value of the number

     Example: digits = [0, 1, 0, 1]   number 5
                base = 2

              returns [0, 1, 1, 0]    number 6
    """

    next_digits = digits.copy()

    # Añade tu código aqui
    # ...
    for i in range(len(next_digits) - 1, -1, -1):
        if next_digits[i] < base - 1:
            next_digits[i] += 1
            break
        else:
            next_digits[i] = 0

    return next_digits


# ----------------------------------------------------------

class My_Iterator:

    def __init__(self, num_digits, base):
        # 2.1 Añade código aqui
        # ...
        self.num_digits = num_digits
        self.base = base

    def next(self):
        # 2.2 Añade código aqui
        # ...
        lista = [0] * self.num_digits
        lista2 = []
        for i in range(0, self.base ** self.num_digits):
            lista2 = lista
            lista = next_number(lista2, self.base)
            yield lista2

        # Cuando no quedan valores simplemente retornamos
        return
