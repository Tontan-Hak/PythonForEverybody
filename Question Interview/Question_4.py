# 4. Write a python program to print a Fibonacci Series
from numpy import maximum


initial_list = [1,2,3,4,-3,4,7,8,9,-6,-2]
new_list = []
while initial_list:
    maximum = initial_list[0]
    for i in initial_list:
        if maximum < i: 
            maximum = i 

    new_list.append(maximum)
    initial_list.remove(maximum)
print(new_list)