# Score
mark = int(input("Enter your marks: "))

if mark >= 80:
    	print("Congratulations, you have scored an A!")

elif mark >= 70:
    	print("Congratulations, you have scored a B!")

elif mark >= 60:
    	print("Congratulations, you have scored a C!")

elif mark >= 50:
    	print("Congratulations, you have scored a D!")
else:
    print("You have scored an F!")
    print("Unfortunately, you did not pass!")

# Vote
citizen = input("Are you a citizen of Australia (y/n)? ")
if citizen == 'n':
    	print("You are not eligible to vote.")
else:
    age = int(input("How old are you (on your last birthday)? "))
if age < 18:
    print("You are too young to vote")
else:
	print("You are eligible to vote")