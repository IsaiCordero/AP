%Planificacion temporal

include "cumulative.mzn";

int:n = 4; % total programas

int:k = 5; % numero total de programadores

int:max_tiempo = 100; % limite superior de tiempo

array [1..n] of int: tiempo = [2,4,6,3];
array [1..n] of int: prog = [3,2,4,2];

output["Total: "++show(total)++"\n"]++[show(comienzo[i])++" " | i in 1..n];

%Introducir el codigo a partir de aqui
array[1..n] of var 0..max_tiempo:comienzo;
var int: total;
constraint cumulative(comienzo, tiempo, prog, k);
constraint forall(i in 1..n)(tiempo[i] + comienzo[i] <= total);
solve minimize total;
