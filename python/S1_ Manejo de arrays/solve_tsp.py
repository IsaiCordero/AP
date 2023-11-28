def order_crossover(parent1, parent2, lower_bound, upper_bound):
    child1 = [0] * len(parent1)
    child1[lower_bound:upper_bound] = parent1[lower_bound:upper_bound]

    lugar_child = upper_bound
    lugar_madre = upper_bound
    while lugar_child != lower_bound:
        if lugar_madre == len(parent2):
            lugar_madre = 0
        if lugar_child == len(child1):
            lugar_child = 0
        if parent2[lugar_madre] not in parent1[lower_bound:upper_bound]:
            child1[lugar_child] = parent2[lugar_madre]
            lugar_child += 1
            lugar_madre += 1
        else:
            lugar_madre += 1

    return child1
