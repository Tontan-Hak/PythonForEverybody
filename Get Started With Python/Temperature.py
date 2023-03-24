# Code 
def convert(f):
    c = (f-32)*5/9
    c = round(c,2)
    return c
def estimate(f): 
    c = (f-30)/2
    c = round(c,2)
    return c
#main
def main():
    for f in range(20, 120, 4):
        print(f, convert(f), estimate(f))
main()   