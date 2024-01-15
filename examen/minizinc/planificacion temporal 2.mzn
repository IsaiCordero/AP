include "globals.mzn";

int:n; % total programas

int:k; % numero total de programadores
int:z; % numero total de analistas

int:max_tiempo; % limite superior de tiempo

array [1..n] of int: tiempo;
array [1..n] of int: programadores;
array [1..n] of int: analistas;

output["Total: "++show(total)++"\n"];

% Activa esta linea si quieres ver cuando comienza cada tarea
% ... pero recuerda desactivarla para evaluar este VPL.
% output [show(comienzo[i])++" " | i in 1..n];


% Introducir el codigo a partir de aqui -------------------------------------

array[1..n] of var 0..max_tiempo:comienzo;
var 0..max_tiempo:total;
constraint cumulative(comienzo,tiempo,programadores,k);
constraint cumulative(comienzo,tiempo,analistas,z);
constraint forall(i in 1..n-1)(comienzo[i] != comienzo[i+1]);
constraint forall(i in 1..n)(comienzo[i] + tiempo[i] <= total);
solve minimize total;

