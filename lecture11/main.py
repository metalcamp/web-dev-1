# simple data types
number = 1  # integer
float = 3.14  # float
string = "this is a string"  # string
is_human = True  # boolean
is_alien = False  # boolean
empty = None

# list
some_list = [1, 34, 25, 35, 26, 4]
# print(some_list)

another_list = ["tesla", "toyota", "mazda"]
# print(another_list)

yet_another_list = [is_alien, is_human]
# print(yet_another_list)

mixed_list = [1, "mazda", False]
# print(mixed_list)

some_list.pop(0)  # removes first element in list
some_list.append(1)  # adds element to list (appends to end)
# print("number of elements in mixed_list: " + str(mixed_list.count(1)))

# print("unsorted some_list")
# print(some_list)
# print("sorted some_list")
some_list.sort()
# print(some_list)

# for item in some_list:
#     if (item != 1):
#         print(item)

# širina / višina / globina
box = [20, 45, 30]
# print(box)
# print(box[0])

box = {
    "height": 20,
    "width": 45,
    "length": 30
}

print(box["height"])
print(box.get("width"))

list = [1, False, "true", None]
list2 = [1, 1, 1, 1] # valid

dict = {
    "pon": "8-17",
    "tor": "8-12",
    "sre": "8-12",
    "čet": "8-12",
    "pet": "8-12",
    "sob": "8-12",
    "ned": "8-12",
}

# invalid dict - contains duplicate keys
dict = {
    "asdfdf1656f5-ffpšsdf-458sdfsdfds": 5,
    "asdfdf1656f5-ffpšsdf-458sdfsdfds": 5,
}
