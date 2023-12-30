int: n = 5;
int: x = 2;
array[1..n] of int: value=[3,10,3,1,2];

% Introduce tu código a partir de esta línea -------------------------
array[1..n] of var 0..1:taken;
constraint forall(i in 1..n-1 where taken[i] == 1)(taken[i+1] != 1);
constraint sum(taken) <= x;
var int: total = sum(i in 1..n)(taken[i] * value[i]);
solve maximize total;
output["taken = ", show(taken), "\n", "total_value = ", show(total)];