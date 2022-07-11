# 1 Write a python program to print Prime Numbers between 2 numbers
for num in range (100,200):
    if all(num%i!=0 for i in range (2,num)):
        print(num)

# 1a Write python program to print how many Prime numbers between 2 numbers
amount = 0 
for num in range (100,201):
    for i in range (2, 100):
        if (num%i==0):
            break
        else:
            amount = amount + 1
print(amount)
