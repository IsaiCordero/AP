# 1. Copia aqui tu solución del primer ejercicio de esta semana

def next_number(digits, base):

    # Añade tu código aqui
    # ...
    for i in range(len(digits)-1, -1, -1):
        if next_digits[i] < base-1:
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
            
        yield next_number(self.num_digits, self.base)
        # Cuando no quedan valores simplemente retornamos
        return
