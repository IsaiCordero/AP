% Use this editor as a MiniZinc scratch book
%TSP Trayecto total mínimo

include "globals.mzn";
int: numCities;          % número de ciudades
set of int: City = 1..numCities; 
int: maxAllowedEdge;     % máxima distancia permitida de un trayecto del recorrido

% distancia entre ciudades 
% -1 significa que no hay conexión directa
array[City,City] of int: distance; 

output ["succ = \(succ)\ntotal_distance = \(total_distance)"];

% Introducir el codigo a partir de aqui ------------------------------------
% Introducir el codigo a partir de aqui ------------------------------------
array[City] of var City: succ;
var int: total_distance;
constraint circuit(succ);
constraint forall(i,j in City where distance[i,j] == -1)(succ[i] != j);
constraint total_distance = sum(i in City)(distance[i,succ[i]]);
solve minimize total_distance;
