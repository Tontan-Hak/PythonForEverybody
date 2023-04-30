# Testing 
friends = ['tontan', 'Pen', 'Cheat']
print(friends[1])

# How long is a list 
greet = "Hello Tontan"
print(len(greet))

# Table of two loop
friends = ["Tontan", "Minh", "Pen", "Tey"]
for friend in friends: 
    print("Happy Khmer New Year: ", friend)
# Other way
fri = ["Rii", "Ro", "Rath"]
for i in range(len(fri)): 
    friend = fri[i]
    print("Happy Khmer New year: ", friend)

# Built -in Functions and List 
numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)

# Other way
total = 0
count = 0
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value     
    count = count + 1

average = total / count
print('Average:', average)