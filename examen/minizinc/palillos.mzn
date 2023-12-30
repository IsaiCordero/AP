include "globals.mzn";

set of int: DIGIT = 1..9;

array[DIGIT] of int: palillos = [1, 2, 3, 4, 5, 2, 3, 4, 5];
int: suma_palillos;

array[1..5] of var DIGIT: x; % 5 incognitas

output["Digitos: \(x)"];

% Escriba su codigo a partir de aqui
constraint sum(i in x)(palillos[i]) = suma_palillos;
constraint alldifferent(x);
constraint (2303 + x[1] * 10) + (980 + x[2] * 1000 + x[3]) = (301 + x[4] * 1000 + x[5] * 10);

solve satisfy;