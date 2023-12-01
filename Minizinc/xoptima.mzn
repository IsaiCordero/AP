var 0..10: x;
constraint x mod 4 == 0;
solve minimize (x-7)^2;
output["x= ", show(x), "\n"];
output["obj=",show((x-7)^2)];