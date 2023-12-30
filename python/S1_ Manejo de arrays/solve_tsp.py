def order_crossover(parent1, parent2, lower_bound, upper_bound):
    child1 = [0] * len(parent1)
    child1[lower_bound:upper_bound] = parent1[lower_bound:upper_bound]
    punteroHijo = upper_bound
    punteroMadre = upper_bound
    while punteroHijo != lower_bound:
        if punteroMadre == len(parent2):
            punteroMadre = 0
        if punteroHijo == len(child1):
            punteroHijo = 0
        if parent2[punteroMadre] not in parent1[lower_bound:upper_bound]:
            child1[punteroHijo] = parent2[punteroMadre]
            punteroHijo += 1
            punteroMadre += 1
        else:
            punteroMadre += 1
    return child1
