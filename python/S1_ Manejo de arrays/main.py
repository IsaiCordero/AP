from solve_tsp import *

string1= input()
parent1 =  [8,11,3,5,6,4,2,12,1,9,7,10]

string2= input()
parent2 =  [1,2,3,4,5,6,7,8,9,10,11,12]

lower_bound = 6
upper_bound = 9

solution = order_crossover(parent1, parent2, lower_bound, upper_bound)

print(solution)