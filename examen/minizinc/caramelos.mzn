int: n = 3;
array[1..n] of int: nota = [7,6,9];        % Puntuación de cada niño; el indice del array
                                 % indica la posición donde está sentado.

int: max_caramelos = 100000;
array[1..n] of var 1..max_caramelos: x; % Número de caramelos dados a cada niño
var int: total_caramelos;        % Número de caramelos totales repartidos por Rosa

output [ show(total_caramelos) ];


% Escribe tu código a partir de aquí
constraint forall(i in 1..n-1 where nota[i] == nota[i+1])(x[i] == x[i+1]);
constraint forall(i in 1..n-1 where nota[i] > nota[i+1])(x[i] > x[i+1] /\ x[i] < x[i+1] * 2);
constraint forall(i in 1..n-1 where nota[i] < nota[i+1])(x[i] < x[i+1]);
constraint total_caramelos = sum(i in 1..n)(x[i]);