int: n;

%Introduzca el código a partir de esta línea
array[1..n] of var 1..9:x;
constraint (sum(x) == product(x));
constraint forall(i in 1..n-1)(x[i] <= x[i+1]);
solve maximize sum(x);