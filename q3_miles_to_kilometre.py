mile = input("Key in distance in miles")

#for i in mile:
#    responses = [int, float]
#    while mile != responses:
#        print("Invalid response!")
#        break

km = float(mile) * 1.60934

if float(mile) == 1:
    print(mile, "mile =", round(km, 3), "km")
else:
    print(mile, "miles =", round(km, 3), "km")
