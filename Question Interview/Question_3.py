# 3. Write a sorting function without using the list.sort function
# from os import remove
# from numpy import minimum


initial_list = [1,2,3,4,-3,4,7,8,9,-6,-2]
new_list = []
while initial_list:
    minimum = initial_list[0]
    for i in initial_list:
        if minimum > i: 
            minimum = i 

    new_list.append(minimum)
    initial_list.remove(minimum)
print(new_list)