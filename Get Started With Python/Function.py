# code
def cylinderVolume(diameter, height):
    from math import pi
    area = pi * diameter**2 / 4
    volume = area * height
    return volume
d = float(input("Enter the can's diameter: "))
h = float(input("Enter the can's height: "))
vol = round(cylinderVolume(d, h), 2)
print("The can’s volume is", vol)