include "globals.mzn";

% Conjunto de vuelos y franjas horarias disponibles
set of int: Flights= 1..5;
set of int: TimeSlots = 1..10;

% Parámetros: Tiempo de inicio y finalización de cada vuelo, capacidad de las franjas horarias
array[Flights] of var TimeSlots: start_time = [1, 2, 3, 4, 5];
array[Flights] of var TimeSlots: end_time = [6, 7, 8, 9, 10];
array[TimeSlots] of int: slot_capacity = [2, 3, 2, 3, 2, 3, 2, 2, 2, 2];

% Variables de decisión: Asignación de franjas horarias a vuelos
array[Flights] of var TimeSlots: assigned_time_slot;

output ["Slots asignados: ", show(assigned_time_slot)];

% ---------- Introducir el código a partir de aquí ---------- 
constraint forall(i in Flights)(assigned_time_slot[i] >= start_time[i]);
constraint forall(i in Flights)(assigned_time_slot[i] <= end_time[i]);
constraint forall(i in TimeSlots)(sum(j in Flights)(assigned_time_slot[j] == i) <= slot_capacity[i]);