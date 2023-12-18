
def solve(num_queens):
    """
    Using backtracking compute all the solutions to place the
    given number of queens in a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """

    solutions_list = []

    # solve it here!
    lista = [0] * num_queens

    def resolver(tabla, fila):
        if fila == num_queens:
            solutions_list.append(list(lista))
            return

        for columna in range(num_queens):
            if salvado(tabla,fila,columna):
                tabla[fila] = columna
                resolver(tabla, fila + 1)
    def salvado(tabla, fila, columna):
        for i in range(fila):
            if tabla[i] == columna:
                return False
            if tabla[i] + i == columna + fila:
                return False
            if tabla[i] - i == columna - fila:
                return False
        return True

    resolver(lista,0)
    return solutions_list
