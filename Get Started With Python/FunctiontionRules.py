# example
def f():
    global message  		
    print("Point A:", message)
    message = "Violets are blue"
    print("Point B:", message)

# main 
message = "Roses are red"
f()
print("Point C:", message)

# If a function defines a variable with the assignment statement, then by default the variable is a Local Variable