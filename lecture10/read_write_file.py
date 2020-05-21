# read from file - example #1
with open("ninja.txt", "r") as ninja_file:
    content = ninja_file.read()
    print(content)

# read from file - example #2
# with open("ninja.txt", "r") as ninja_file:
#     ninja_lines = ninja_file.readlines()
#
#     for line in ninja_lines:
#         print(line)

# write to file
# with open("ninja2.txt", "w") as ninja_file_2:
#     ninja_file_2.write("Hello, yet another new file!")

# append to file
# with open("ninja2.txt", "a") as ninja_file_2:
#     ninja_file_2.write("\nHello, this is appended text!")
