int: num_nodes = 9;                          % número de nodos del grafo
int: num_edges = 14;                          % número de aristas del grafo

1..num_nodes:source = 1;                     % nodo fuente
1..num_nodes:sink = 9;                       % nodo sumidero

array[1..num_edges, 1..2] of int: edges = array2d(1..num_edges, 1..2,
[
       1, 2, 
       1, 4,
       2, 3,
       2, 4,
       3, 5,
       3, 8,
       4, 5,
       5, 2,
       5, 6,
       5, 7,
       6, 7,
       6, 8,
       7, 9,
       8, 9]); % aristas del grafo (origen->destino)
array[1..num_edges] of int: capacity = [14,23,10, 9,12,18,26,11,25, 4, 7, 8,15,20];    % capacidad de cada arista

var int: max_flow;                       % variable de decision para el valor
                                         % del flujo máximo
array[1..num_edges] of var int: flow;    % variable de decisión para el flujo
                                         % final de cada arista

output
[ 
  "max flow =" ++ show(max_flow)
];

% Escribir el código a partir de aquí-----------------------------------------

constraint forall(i in 1..num_edges)(flow[i] >= 0);
constraint forall(i in 1..num_edges)(flow[i] <= capacity[i]);
constraint forall(i in 1..num_edges where i != source /\ i != sink)(sum(j in 1..num_edges where edges[j,1] == i)(flow[j]) == sum(k in 1..num_edges where edges[k,2] == i)(flow[k]));
constraint max_flow = sum(i in 1..num_edges where edges[i,2] == sink)(flow[i]);
solve maximize max_flow;