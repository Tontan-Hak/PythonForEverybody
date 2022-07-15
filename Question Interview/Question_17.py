# 17. Write a program to check whether an integer number is a Palindrome or not
number = int(input("Enter the integer number: "))
temp = number
reverse_number = 0
while(number>0):
    remainder = number % 10
    reverse_number = (reverse_number * 10) + remainder
    number = number // 10 
print("The reverse of integer number: ", reverse_number)

if (reverse_number==temp):
    print("True")
else: 
    print("False")
# def isPalindrome(s):
#     return s == s[::-1]
 
 
# # Driver code
# s = "malayalam"
# ans = isPalindrome(s)
 
# if ans:
#     print("Yes")
# else:
#     print("No")