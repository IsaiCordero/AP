

class My_Iterator:

    def __init__(self, num_digits, minimos, maximos):
        self.num_digits = num_digits
        self.minimos = minimos
        self.maximos = maximos
        self.current = [minimos[i] for i in range(num_digits)]
        #se crean las variables para los valores maximos y minimos(dos listas) y la lista que será retornada con un yield
    def incrementar(self):
        j = self.num_digits - 1
        while j >= 0:
            self.current[j] += 1
            #se van sumando valores en la posicion de la lista, si este es menor o igual que el maximo sigue con las iteraciones
            if self.current[j] <= self.maximos[j]:
                break
            #si es mayor, vuelve a su valor minimo
            else:
                self.current[j] = self.minimos[j]
                j -= 1
        return j >= 0
    
    def next(self):
        while True:
            yield list(self.current)
            if not self.incrementar():
                break
