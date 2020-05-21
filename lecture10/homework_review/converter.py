factor = 0.621371

print("Unit converter helps us converting kilometers to miles")

while True:
    kilometers = float(input("Enter kilometers:"))
    miles = round(kilometers * factor, 2)
    print("{0} km equals {1} miles".format(kilometers, miles))

    answer = input("Would you like to make another conversion? ")

    if "y" not in answer.lower():
        print("Bye!")
        break
