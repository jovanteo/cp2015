number = int(input("key in a whole number: "))
stop = number
factors = []
factor = 2
while factor < stop/2 +1:
    if number % factor == 0:
        factors.append(factor)
        number /= factor
    else:
        factor += 1
    
print(factors)
