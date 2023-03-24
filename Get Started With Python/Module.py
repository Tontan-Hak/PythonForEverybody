# Use module 
def convert(f): 
    c = (f-32)*5/9
    c = round(c,2)
    return c
def estimate(f): 
    c = (f-32)/2
    c = round(c, 2)
    return c
def main():
    for f in range(60,101, 5):
        print(f,convert(f), estimate(f))

if __name__=="__main__":
    main()

# Note that when we inport module conversion, the main function is called and executed
# We can suppress this call when we import the module by putting the call inside a special if statement 