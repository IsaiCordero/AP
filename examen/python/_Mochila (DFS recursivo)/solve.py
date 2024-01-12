def solve(items, capacity):
    def dfs(indice, current_capacity, current_value, current_taken):
        nonlocal taken
        nonlocal value

        #si exploramos todos los elementos, comprobamos si la solucion es mejor
        if indice == len(items):
            if current_value > value:
                value = current_value
                taken = current_taken.copy()
            return

        #comprobamos si el elemento actual cabe en la mochila para asi poder introducirlo
        valor, peso = items[indice]
        if current_capacity >= peso:
            dfs(indice + 1, current_capacity - peso, current_value + valor, current_taken + [indice + 1])

        dfs(indice + 1, current_capacity, current_value, current_taken)

    value = 0
    taken = []
    dfs(0, capacity, 0, [])
    return taken, value