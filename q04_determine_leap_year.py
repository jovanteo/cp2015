x = 1
while x != 0:

    year = (input("Key in year: "))

    while True:
        try:
            years = int(year) % 400
            while years == 0:
                print(year, "is leap year")
                break
            else:
                years = int(year) % 100
                while years == 0:
                    print(year, "is not a leap year")
                    break
                else:
                    years = int(year) % 4
                    while years == 0:
                        print(year, "is leap year")
                        break
                    else:
                        print(year, "is not leap year")
        except ValueError:
            print("input a numeric year")
        break
