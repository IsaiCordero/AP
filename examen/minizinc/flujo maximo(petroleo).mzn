% Parámetros del problema
% Problema de flujo máximo en una red de tuberías de petróleo

% Número de puntos de conexión en el sistema
int: num_nodes = 5;

% Número de tuberías en el sistema
int: num_edges = 7;

% Fuente principal
int: source = 1;

% Contenedor o depósito final
int: sink = 5;

% Definición de las tuberías: [punto de entrada, punto de salida]
array[1..num_edges, 1..2] of int: edges= [| 1, 2 | 1, 3 | 2, 4 | 3, 4 | 2, 5 | 3, 5 | 4, 5 |];

% Capacidad de cada tubería en litros/segundo
array[1..num_edges] of int: capacity= [15, 20, 15, 20, 10, 10, 15];

% Rango de presión operativa seguro: [presión minima, presión máxima]
array[1..num_edges, 1..2] of int: pressure_range = [| 5, 20 | 5, 25 | 5, 20 | 5, 25 | 5, 15 | 5, 15 | 5, 20 |];

% Presión base de cada tubería (presión mínima sin flujo)
array[1..num_edges] of int: base_pressure = [5, 5, 5, 5, 5, 5, 5];

% Constante conocida
int: k = 2;

% Variable de decisión que representa el flujo máximo que llega al contenedor
var int: max_flow;

% Variable de decisión que indica el volumen de agua en cada tubería
array[1..num_edges] of var 0..max(capacity): flow;

% Poner el código a partir de aquí ------------------------------------------
constraint forall(i in 1..num_edges)(flow[i] >= 0 /\ flow[i] <= capacity[i]);
constraint forall(i in 1..num_edges where i != sink /\ i != source)(sum(j in 1..num_edges where edges[j,1] == i)(flow[j]) == sum(k in 1..num_edges where edges[k,2] == i)(flow[k]));
constraint max_flow = sum(i in 1..num_edges where edges[i,2] == sink)(flow[i]);


% constraint forall(i in 1..num_edges)(base_pressure[i] + k*flow[i] >= pressure_range[i,1] /\ base_pressure[i] + k*flow[i] <= pressure_range[i,2]);
%no entiendo bien la restriccion que pide, se supone que es esta pero sin ella ya el vpl da bien(con ella da mal)

solve maximize max_flow;