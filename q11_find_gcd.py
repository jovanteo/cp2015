x=1
while x != 0:

    n1 = int(input("enter an integer"))
    n2 = int(input("enter another integer"))

    d = min(n1, n2)
    while d > 0:
        if n1 % d == 0:
            if n2 % d == 0:
                print(d)
                break
        d -= 1
    break
