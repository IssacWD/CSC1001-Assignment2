def isValid(number):
    if number % 10 == 0:
        return True
    else:
        return False

def sumOfDoubleEvenPlace(number):
    even_place = number[-2::-2]
    sum = 0
    for i in even_place:
        sum += getDigit(str(int(i)*2))
    return sum

def getDigit(number):
    if int(number) < 10:
        return(int(number))
    else:
        sum_digit = int(number[0]) + int(number[1])
        return(sum_digit)

def sumOfOddPlace(number):
    odd_place = number[::-2]
    sum = 0
    for i in odd_place:
        sum += int(i)
    return sum

while True:
    n = input("Please enter your credit card number as an integer:")
    if n.isdigit():
        break

if isValid(sumOfDoubleEvenPlace(n) + sumOfOddPlace(n)):
    print("The credit card number is valid.")
else:
    print("The credit card number is invalid.")