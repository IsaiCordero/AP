def solve_tabulation(items):
    table = []
    taken = []

    def fill_table():
        nonlocal table
        table = [0] * (len(items) + 1)
        table[1] = items[0]

        for i in range(2, len(items) + 1):
            table[i] = max(table[i - 2] + items[i - 1], table[i - 1])

    def fill_taken():
        nonlocal taken
        taken = []
        i = len(items)
        while i >= 1:
            #si se encuentra en la ultima posicion de la tabla o si el valor de la casa actual es mayor que el de la siguiente, robará esa casa
            #esto es muy parecido al memoization con el tema de la tabla(en el ejercicio de la mochila esto es mas diferente)
            if i == 1 or table[i - 2] + items[i - 1] > table[i - 1]:
                taken.append(i)
                i -= 2
            else:
                i -= 1
        taken.reverse()

    fill_table()
    fill_taken()
    return table[len(items)], taken
