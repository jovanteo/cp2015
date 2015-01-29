#an integer between 0 and 1000 and adds all the digits in the integer. For
#example, if an integer is 932, the sum of all its digits is 14.
#Hint: Use the % operator to extract digits, and use the // operator to remove
#the extracted digit. For instance, 932 % 10 = 2 and 932 // 10 = 93 

number = int(input("Input num between 0 and 1000): "))

def sumof(number):
    total_sum = 0
    while 0 < number < 1000:
        total_sum += (number % 10)
        number = number // 10
    return total_sum

print(sumof(number))