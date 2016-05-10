# 2 3 5 7 9 11 13 17 19 23
def isprime(number):
    if number == 2:
        return True
    elif number == 1:
        return False
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5)+1, 2):
            if number % i == 0:
                return False
        return True

number = 10000
x = []
for i in range(number):
    if isprime(i):
        x.append(i)
print(x)


def evenprimesum(number):
    for i in range(4, number, 2):
        havesum = False
        for j in range(len(x)):
            for k in range(len(x)):
                answer = x[j] + x[k]
                if answer == i:
                    print(x[j],"+", x[k], '=', i)
                    havesum = True
                if havesum:
                    break
            if havesum:
                break
        if not havesum:
            return False
    print("But why use this limit????")
    return True

print(evenprimesum(number))

