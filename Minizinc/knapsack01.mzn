int:n; 
int: capacity; 
set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

%Escribir el código a partir de aquí
array[1..n] of var 0..1: taken;
constraint sum(i in 1..n)(taken[i] * weight[i]) <= capacity;
solve maximize sum(i in 1..n)(taken[i] * value[i]);
output["taken = ",show(taken),"\n"];
output["Total Value = ", show(sum(i in 1..n)(taken[i] * value[i]))]