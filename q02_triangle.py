while True:
    try:
        side1 = input("Input a side")
        side2 = input("Input another side")
        side3 = input("Input another side")
        side1, side2, side3 = [float(side1), float(side2), float(side3)]
        sides = side1, side2 , side3
        ssides = sum(sides)

        if side1+side2 <= side3 or side1+side3 <= side2 or side3+side2 <= side1:
            print("invalid")
        else:
            print(ssides)
    except ValueError:
        print("input a legit number")
