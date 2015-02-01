num = input("key in a positive integer: ")

def number():
    if not num.isnumeric():
        print("key in a",'\033[1m' + 'POSITIVE INTEGER!!')
# How do i make user rekey
    elif int(num) == 0 or int(num) % 2 == 0:
        print("Number is even")

    else:
        print("Number is odd")

number()
