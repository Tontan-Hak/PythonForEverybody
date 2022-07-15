# 18. Write a program to check number reepresentation is in binary

number = int(input("Enter the integer number: "))
#temp = number
while number != 0:
    remainder = number % 10
    if(remainder !=0 and remainder !=1):
        print('Number is not in binary representation!')
        break
    number = number // 10
    if (number==0):
        print("Number is in binary represesntation!")
