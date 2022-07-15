# 16 Write a program to reverse an integer number

number = int(input("Enter the integer number: "))
reverse_number = 0
while(number>0):
    remainder = number % 10
    reverse_number = (reverse_number * 10) + remainder
    number = number // 10 
print("The reverse of integer number: ", reverse_number)






