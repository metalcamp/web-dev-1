with open("file.csv", "r") as file:
    lines = file.readlines()
    content_lines = lines
    content_lines.pop(0)

    for line in content_lines:
        line_list = line.split(",")
        name = line_list[0]
        gender = line_list[2]
        age = line_list[1]
        print(name + " is " + gender + " and " + age + " years old.")
