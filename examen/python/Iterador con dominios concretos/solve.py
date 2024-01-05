class My_Iterator:

    def __init__(self, num_digits, digit_values):
        self.num_digits = num_digits
        self.digit_values = digit_values

    def next(self):
        indices = [0] * self.num_digits
        while True:
            lista = [self.digit_values[i][indices[i]] for i in range(self.num_digits)]
            yield lista

            #actualizas el valor de la primera posicion
            indices[self.num_digits - 1] += 1


            # compruebas si ya está en el ultimo valor para esa posicion
            for i in range(self.num_digits - 1, - 1, - 1):
                if indices[i] == len(self.digit_values[i]):
                    if i != 0:
                        indices[i] = 0
                        indices[i - 1] += 1
                    else:
                        return