# rectangle 5x5
print("5x5\n")
width = 5
for i in range(width):
    print(width * "*")

# rectangle 10 x 4
print("\n10x4\n")
width = 10
length = 4
for i in range(length):
    print(width * "*")

# triangle 1
print("\ntriangle 1\n")
length = 6
for i in range(length):
    print(i * "*")

print("\ntriangle 2\n")
max_width = 5
counter = 0

while counter < max_width:
    print((max_width - counter) * "*")
    counter = counter + 1
