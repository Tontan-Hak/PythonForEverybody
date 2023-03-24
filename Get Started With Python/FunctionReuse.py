# From conversion inport convert
def convert(f):
    c = (f-32)*5/9
    c = round(c,2)
    return c
tem = int(input("Enter current temperature in F:"))
print("The temperature in C:" , convert(tem))