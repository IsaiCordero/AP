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
    iteracion = My_Iterator(num_queens,num_queens)
    for valor in iteracion.next():
        valido = True
        for i in range(num_queens):
            if not servible(valor, i, valor[i]):
                valido = False
                break
        if valido:
            solutions_list.append(valor)

    return solutions_list

def servible(valor, i, j):
    for k in range(i):
        if valor[k] == j:
            return False
        if valor[k] + k == j + i:
            return False
        if valor[k] - k == j - i:
            return False

    return True