from sys import maxsize as infinite

def solve(coins, change):
    lista = sorted(coins, reverse = True)
    result = []
    final = []
    for i in range(len(lista)):
        if lista[i] <= change:
            change -= lista[i]
            result.append(lista[i])

    for i in result:
        for j in range(len(coins)):
            if i == coins[j]:
                if j+1 not in final:
                    final.append(j+1)
    return final
