# List testing 
numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)
# List and define loops
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends: 
    print("Happy Khmer New year: ", friend)
print("Done")