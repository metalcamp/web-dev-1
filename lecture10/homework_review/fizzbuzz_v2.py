inputNumber = 0

def fizzbuzz(number):
    if number % 15 == 0:
        return "fizzbuzz"
    elif number % 5 == 0:
        return "buzz"
    elif number % 3 == 0:
        return "fizz"
    else:
        return str(number)

while inputNumber < 1 or inputNumber > 100:
    inputNumber = int(input("Select number between 1 and 100: "))

for number in range(1, inputNumber + 1):
    result = fizzbuzz(number)
    print(result)
