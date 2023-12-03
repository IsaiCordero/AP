int:n;                    % numero maximo de items
int: capacity;            % capacidad de la mochila

set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

set of ITEMS: limitation;
int:m;                    % Numero maximo de items a elegir dentro del 
                          % conjuto limitation

% Escribe el código a partir de aquí ----------------------------------
var set of ITEMS: taken;

constraint sum(i in taken)(weight[i])<= capacity;
constraint card(taken intersect limitation) <= m;
solve maximize sum(i in taken)(value[i]);

output[show(taken), "\n"];
output[show(sum(i in taken)(value[i]))]
