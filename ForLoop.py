#
# Define a list of numbers
numbers = [10, 20, 30, 40]
# Display the numbers in the list one by one
for n in numbers:
    	print(n)		# line 6
	
# code
marks = [60, 50, 40, 20, 90]
count = 0
for m in marks:
    if m >= 50:
        print(m)
        count = count + 1
passRate = count / len(marks)
print("The pass rate is", round(passRate * 100), "%")
# 
start = 1
end = 16
for n in range(start, end+1):
	print(n, 2**n)