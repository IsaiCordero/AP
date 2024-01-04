

import numpy as np
def solve_tabulation(items, capacity):
    taken = []
    table = np.zeros((len(items)+1, capacity+1), dtype=int)

    def fill_table():
        for i in range(1, len(items) + 1):
            for j in range(capacity + 1):
                item_index = i - 1
                item_value = items[item_index].value
                item_weight = items[item_index].weight

                if item_weight <= j:
                    table[i][j] = max(table[i-1][j], item_value + table[i-1][j - item_weight])
                else:
                    table[i][j] = table[i-1][j]

    def fill_taken():
        i = len(items)
        j = capacity
        cont = 0
        while i > 0 and j > 0:
            if table[i][j] != table[i-1][j]:
                taken.insert(0, i)
                j -= items[i-1].weight
            else:
                cont += 1
            i -= 1

    fill_table()
    fill_taken()
    return table[-1][-1], taken
