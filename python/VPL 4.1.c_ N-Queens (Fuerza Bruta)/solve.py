from my_iterator import *

def solve(num_queens):
    """
    Using your brute force iterator compute all the
    solutions to place the given number of queens in
    a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """

    solutions_list = []

    # solve it here!
    iterador = My_Iterator(num_queens,num_queens)
    for valores in iterador.next():
        valido = True
        for i in range(num_queens):
            if not servible(valores, i, valores[i]):
                valido = False
                break
        if valido:
            solutions_list.append(valores)

    return solutions_list
def servible(tabla, fila, columna):
    for i in range(fila):
        if tabla[i] == columna:
            return False
        if tabla[i] + i == columna + fila:
            return False
        if tabla[i] - i == columna - fila:
            return False
    return True