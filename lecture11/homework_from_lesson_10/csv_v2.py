with open("file.csv", "r") as person_file:
    person_lines = person_file.readlines()

    for line in person_lines[1:]:
        line = line.strip()
        person = line.split(',')
        name = person[0]
        gender = person[2]
        age = person[1]
        print(name + " is " + gender + " and " + age + " years old.")