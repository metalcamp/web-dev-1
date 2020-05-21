import random

min = 1
max = 50
secret = random.randint(min, max)
guess = 0

# while guess != secret:
#     guess = int(input("Ugani skrito stevilo (med " + str(min) + "in " str(max) + "):"))
#     if guess == secret:
#         print("Bravo, zadel si skrito stevilo")
#     else:
#         print("Poskusi ponovno")

# for x in range(3):
#     # print("stevec: " + str(x))
#     guess = int(input("Ugani skrito stevilo (med 1 in 30):"))
#     if guess == secret:
#         print("Bravo, zadel si skrito stevilo")
#         break
#     else:
#         print("Poskusi ponovno")

# while True:
#     guess = int(input("Ugani skrito stevilo (med 1 in 50):"))
#     if guess == secret:
#         print("Bravo, zadel si skrito stevilo")
#         break
#     elif guess > secret:
#         print("poskusi z manjsim stevilom")
#     elif guess < secret:
#         print("poskusi z vecjim stevilom")