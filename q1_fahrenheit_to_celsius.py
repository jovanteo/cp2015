Fahrenheit = input("Key in temperature in F: ")

if Fahrenheit.isdigit():
    Celsius = (float(Fahrenheit) - 32) * 5/9
    print(Fahrenheit, "degree Fahrenheit =", Celsius, "degree Celsius")
else:
    print("Invalid, please rekey")
