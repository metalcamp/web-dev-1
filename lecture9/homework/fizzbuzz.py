number = 0

while number < 1 or number > 100:
    number = int(input("Select number between 1 and 100: "))

for num in range(1, number+1):
    if num % 15 == 0:
        print("fizzbuzz")
        continue
    elif num % 3 == 0:
        print("fizz")
        continue
    elif num % 5 == 0:
        print("buzz")
        continue
    else:
        print(num)