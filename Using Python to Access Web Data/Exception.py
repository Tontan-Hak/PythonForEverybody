# Example of exception
# T = int(input("Enter an integer: "))
# print("The number you enter is ", T)
#print("Bye!")

# 
def main():
    try:
        weight = int(input("Enter the weight in kg: " ))   
        heightInCM = int(input("Enter your height in cm: "))
        bmi = calculateBMI(weight, heightInCM);
        print("BMI: {:.2f}".format(bmi))
        ...

    except:
        print("Some input is in wrong format or outside valid range!")
        print("Please try again.")

main()