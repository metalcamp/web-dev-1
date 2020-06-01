# BasketballPlayer
# name
# position
# height
# number
# age
# points
# assists
# rebounds
# weight

# Excel table header would look like line below
# name, position, height, ...
# Lebron James, center, 205cm,...


class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        # pounds = self.weight * 2.20
        # return pounds
        return round(self.weight_kg * 2.20, 2)


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, position, height_cm, dressNumber, age, points, assists, rebounds,
                 weight_kg):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.position = position
        self.dressNumber = dressNumber
        self.age = age
        self.points = points
        # self.points = BasketballPoint(number=3)
        self.assists = assists
        self.rebounds = rebounds

    def increasePoints(self, points):
        # TODO validation
        self.points += points

    def decreasePoints(self, points):
        # TODO validation
        self.points -= points


class BasketballPoint():
    def __init__(self, number):
        if 0 < number < 3:
            self.number = number
        else:
            ValueError("Try again")


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, weight_kg, height_cm, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


lebron = BasketballPlayer(first_name='Lebron', last_name='James', position='center', height_cm=203, dressNumber=22,
                          age=30,
                          points=500,
                          assists=425, rebounds=120, weight_kg=110)

# kevin_durant = BasketballPlayer(first_name='Kevin', last_name='Durant', position='center', height_cm=190,
#                                 dressNumber=22,
#                                 age=30, points=500,
#                                 assists=425, rebounds=120, weight_kg=100)

messi = FootballPlayer(first_name='Lionel', last_name='Messi', height_cm=170, weight_kg=70, goals=570, yellow_cards=50,
                       red_cards=1)

# lebron_dict = {'name': 'Lebron James', 'position': 'center', 'height': 203}

# print(round(lebron.weight_to_lbs(), 2))
# print(round(kevin_durant.weight_to_lbs(), 2))

print(lebron.first_name)
print(lebron.last_name)
print(lebron.weight_to_lbs())

numPoints = 3
lebron.increasePoints(numPoints)

print(messi.first_name)
print(messi.last_name)
print(messi.weight_to_lbs())
