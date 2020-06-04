import random
from datetime import datetime
from prettytable import PrettyTable

random_num = random.randint(1, 50)
# print(random_num)

time_now = datetime.now()
# print(time_now)

table = PrettyTable(['animal', 'ferocity'])
table.add_row(['grizzly', 87])
table.add_row(['wolverine', 100])
table.add_row(['cat', -1])
table.add_row(['dolphin', 60])


# print(table)


def sumHelper(x, y, z):
    return x + y + z


class Box():
    def __init__(self, x=1, y=1, z=1):
        self.x = x
        self.y = y
        self.z = z

    def sum(self):
        return self.x + self.y + self.z

    def volume(self):
        return self.x * self.y * self.z

    def save_to_file(self):
        with open('mybox.txt', 'w') as file:
            var = file.read()
            var = var + str(self.__dict__)
            file.write(var)

    def sum_and_print(self):
        print("box sum: {0}".format(self.sum()))


class ColorBox(Box):
    def __init__(self, x, y, z, color):
        super().__init__(x, y, z)
        self.color = color


class ColorBox2(ColorBox):
    def __init__(self, x, y, z, color1, color2):
        super().__init__(x, y, z, color1)
        self.color2 = color2


class ColorBox3(ColorBox2):
    def __init__(self, x, y, z, color1, color2, color3):
        super().__init__(x, y, z, color1, color2)
        self.color3 = color3


class Player():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return self.name + " " + self.surname

    def __str__(self):
        return self.name + " " + self.surname


class Team():
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)


box = Box(1, 2, 3)  # required args
box2 = Box(2, 4, 6)  # optional args
colorBox = ColorBox(1, 2, 3, 'green')
colorBoxWithTwoColors = ColorBox2(1, 2, 3, 'green', 'blue')
colorBoxWithThreeColors = ColorBox3(1, 2, 3, 'green', 'blue', 'red')

print(box.__dict__)
print(box2.__dict__)
print(colorBox.__dict__)
print(colorBoxWithTwoColors.__dict__)
print(colorBoxWithThreeColors.__dict__)

team = Team('NK Olimpija')
print(team.players)
team.add_player(Player(name="Janez", surname="Novak"))
print(team.players)
