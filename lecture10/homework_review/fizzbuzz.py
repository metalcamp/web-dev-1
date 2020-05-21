inputNumber = 0

while inputNumber < 1 or inputNumber > 100:
    inputNumber = int(input("Select number between 1 and 100: "))

for number in range(1, inputNumber + 1):
    if number % 15 == 0:
        print("fizzbuzz")
        continue
    elif number % 5 == 0:
        print("buzz")
        continue
    elif number % 3 == 0:
        print("fizz")
        continue
    else:
        print(number)

