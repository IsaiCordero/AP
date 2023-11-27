def order_crossover(parent1, parent2, lower_bound, upper_bound):
    child1 = [0] * len(parent1)
    child1[lower_bound:upper_bound] = parent1[lower_bound:upper_bound]

    puntero_hijo = upper_bound
    puntero_madre = upper_bound

    while puntero_hijo != lower_bound:
        if puntero_madre == len(parent2):
            puntero_madre = 0
        if puntero_hijo == len(child1):
            puntero_hijo = 0
        if parent2[puntero_madre] not in parent1[lower_bound:upper_bound]:
            child1[puntero_hijo] = parent2[puntero_madre]
            puntero_madre += 1
            puntero_hijo += 1
        else:
            puntero_madre += 1

    return child1
