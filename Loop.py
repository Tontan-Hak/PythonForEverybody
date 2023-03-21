# While Loop
n = 1
while n<=100:
    print(n)
    n = n + 1

# code
response = "y"
while response == "y":
    print("Hello!")
    response = input("Continue? (y/n): ")

# code
keepLooping = True
while keepLooping: 
    print("Hello")
    userResponse = input("Continue?(y/n): ")
    keepLooping = userResponse == "y"

# code
while True: 
    print("Hello")
    userResponse = input("Continue?(y/n): ")
    if userResponse != "y":
        break