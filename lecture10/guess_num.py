import random

min = 1
max = 5
secret = random.randint(min, max)
guess = 0
attempts = 0

with open("score.txt") as score_file:
    best_score = int(score_file.read())
    print("Best score: {0} attempt(s)".format(best_score))

while True:
    guess = int(input("Ugani skrito stevilo (med {0} in {1}):".format(min, max)))
    attempts += 1

    if guess == secret:
        print("Bravo, zadel si skrito stevilo")
        if attempts < best_score:
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))
        break
    elif guess > secret:
        print("poskusi z manjsim stevilom")
    elif guess < secret:
        print("poskusi z vecjim stevilom")

print("You have attempted {0} time(s)".format(attempts))


###################
