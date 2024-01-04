import numpy as np

# Función principal para resolver el problema de la mochila mediante tabulación
def solve_tabulation(items, capacity):
    taken = []  # Lista para almacenar los índices de elementos seleccionados
    table = np.zeros((len(items) + 1, capacity + 1), dtype=int)  # Tabla para almacenar resultados intermedios

    # Llena la tabla con los valores óptimos
    def fill_table():
        for i in range(1, len(items) + 1):
            for j in range(capacity + 1):
                index = i - 1
                value = items[index].value  # Valor del elemento actual
                weight = items[index].weight  # Peso del elemento actual
                if weight <= j:
                    # Si el peso del elemento es menor o igual a la capacidad actual,
                    # calcula el máximo entre tomar o no tomar el elemento en la mochila
                    table[i][j] = max(table[i - 1][j], value + table[i - 1][j - weight])
                else:
                    # Si el peso del elemento es mayor que la capacidad actual,
                    # simplemente hereda el valor anterior
                    table[i][j] = table[i - 1][j]

    # Reconstruye los elementos seleccionados para la mochila óptima
    def fill_taken():
        i = len(items)
        j = capacity
        while i > 0 and j > 0:
            if table[i][j] != table[i - 1][j]:
                taken.insert(0, i)  # Inserta el índice del elemento seleccionado
                j -= items[i - 1].weight  # Resta el peso del elemento seleccionado
            else:
                i -= 1

    fill_table()  # Llena la tabla con los valores óptimos
    fill_taken()  # Reconstruye los elementos seleccionados
    return table[-1][-1], taken  # Devuelve el valor máximo y la lista de elementos seleccionados
