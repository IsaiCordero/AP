from functools import lru_cache

def solve(graph, from_node, to_node):
    #se usa para el memoization y almacenar resultados
    @lru_cache(maxsize=None)
    def dfs(node):
        #si es el nodo destino la ruta es unicamente esta
        if node == to_node:
            return 0, [to_node]

        minDistance = float('inf')
        minPath = []
        #se itera sobre los vecinos del nodo actual y se llama a la funcion dfs calculando la distancia total
        for vecinos, pesos in graph[node].items():
            distance,path = dfs(vecinos)
            totalDistance = distance + pesos['weight']
            #si esta distancia es mas corta, se actualizan los valores
            if totalDistance < minDistance:
                minDistance = totalDistance
                minPath = [node] + path
        return minDistance,minPath
    #se llama al dfs y si la distancia sigue siendo infinita, no hay ruta
    min_d, path = dfs(from_node)
    if min_d == float('inf'):
        return "No path exists"
    return min_d,path
    