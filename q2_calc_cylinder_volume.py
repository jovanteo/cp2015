radius = input("Lets find the volume of a cylinder! Radius please")
length = input("now length please")

from math import pi
area = float(radius) * float(radius) * pi
volume = area * float(length)

print("Therefore volume when length is", length, "and radius is", radius, volume)