def solve_memoization(items):
    mem = {}
    taken = []

    def t(n):
        if n < 0:
            return 0
        if n in mem:
            return mem[n]
        #crea la tabla con los valores maximos desde n posicion
        mem[n] = max(t(n - 2) + items[n], t(n - 1))
        return mem[n]

    def fill_taken():
        nonlocal taken
        i = len(items) - 1
        while i >= 0:
            if i == 0:
                taken.append(i)
                break
            #si el valor de la tabla actual es el mismo que el siguiente significará que el actual no lo pilla
            if mem[i] == mem[i - 1]:
                i -= 1
            #si el valor actual es mayor que el siguiente, entonces significará que robó esa casa
            else:
                taken.append(i)
                i -= 2
        taken.reverse()

    n = len(items) - 1
    max_benefit = t(n)
    fill_taken()

    return max_benefit, taken
