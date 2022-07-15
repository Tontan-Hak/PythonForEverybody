# 16 Write a program to reverse an integer number
number = int(input("Enter the integer number: "))
revs_number = 0
while(number>0):
    R = number % 10
    revs_number = (revs_number * 10) + R
    number = number // 10 
print(revs_number)






