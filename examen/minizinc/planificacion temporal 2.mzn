include "globals.mzn";
include "cumulative.mzn";
int:n = 4; % total programas

int:k = 5; % numero total de programadores
int:z = 4; % numero total de analistas

int:max_tiempo = 20; % limite superior de tiempo

array [1..n] of int: tiempo=[2,4,6,3];
array [1..n] of int: programadores=[3,2,4,2];
array [1..n] of int: analistas=[2,2,2,2];

output["Total: "++show(total)++"\n"];

%output [show(comienzo[i])++" " | i in 1..n];


% Introducir el codigo a partir de aqui -------------------------------------
array[1..n] of var 0..max_tiempo: comienzo;
constraint cumulative(comienzo, tiempo, programadores, k);
constraint cumulative(comienzo, tiempo, analistas, z);
constraint forall(i in 1..n-1)(comienzo[i] != comienzo[i+1]);
var 1..max_tiempo: total;
constraint forall(i in 1..n)(tiempo[i] + comienzo[i] <= total);
solve minimize total;
