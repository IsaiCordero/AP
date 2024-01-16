% Job Shop Scheduling (JSP)

include "globals.mzn";

int : n = 3;
array[1..n] of int: duration = [6,4,5];
array[1..n] of int: due_date = [8,4,12];

output["start = \(start)\n"];
output["resources = \(resources)\n"];
output["delay = \(delay)\n"];
output["total_delay = \(total_delay)\n"];

% Resuelve tu ejercicio aqui ------------------------------------
array[1..n] of var 0..1000:start;
array[1..n] of var int:delay;
array[1..n] of var int:resources;
var int:total_delay;

constraint forall(i in 1..n)(resources[i] = 1);
constraint forall(i in 1..n)(delay[i] = max(0,((start[i] + duration[i]) - due_date[i])));
constraint cumulative(start, duration, resources, 1);
constraint total_delay = sum(delay);
solve minimize total_delay;