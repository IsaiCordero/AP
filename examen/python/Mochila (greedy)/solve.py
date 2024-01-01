def solve(items, capacity):
    # Calcula la densidad para cada elemento y ordénalos por densidad en orden descendente
    lista = items.copy()
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    taken = []
    value = 0

    for valor, peso in items:
        if peso <= capacity:
            taken.append(lista.index((valor, peso)) + 1)
            value += valor
            capacity -= peso

    return taken, value
