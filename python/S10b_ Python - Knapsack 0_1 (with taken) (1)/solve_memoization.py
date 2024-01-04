def solve_memoization(items, capacity):
    taken = []
    mem = {}

    def t(n, w):
        if n < 0 or w <= 0:
            return 0

        if (n, w) in mem:
            return mem[(n, w)]

        # Verificar si el peso del artículo actual es menor o igual a la capacidad restante
        if items[n].weight > w:
            result = t(n - 1, w)
        else:
            # Considerar el caso de tomar o no tomar el artículo actual
            take_item = items[n].value + t(n - 1, w - items[n].weight)
            leave_item = t(n - 1, w)
            result = max(take_item, leave_item)

        mem[(n, w)] = result
        return result

    def fill_taken():
        n = len(items) - 1
        w = capacity
        cont = 0
        while n >= 0 and w >= 0:
            if (n, w) not in mem:
                break  # Terminar el bucle si la clave no está en el diccionario

            if n == 0 and mem[(n, w)] > 0:
                taken.insert(0, n)
            elif mem[(n, w)] != mem.get((n - 1, w), 0):
                taken.insert(0, n+1)
                w -= items[n].weight
            else:
                cont += 1
            n -= 1
    max_benefit = t(len(items) - 1, capacity)
    fill_taken()

    return max_benefit, taken
