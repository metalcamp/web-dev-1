# function prints welcome message - name required
def say_hello_with_name(name):
    print("Hello, {0}!".format(name))


# function prints welcome message - name optional
def say_hello(name=None):
    if name is not None:
        print("Hello, {0}!".format(name))
    else:
        print("Hello!")


# function returns message
def say_hello_2(name):
    return "Hello, {0}!".format(name)


# write a function which gets two numbers as input and returns sum of these numbers
def calculate_sum(a, b):
    # result = a + b
    # return result
    return a + b


# write a function which gets one number as input and return cube of that number
def calculate_cube(a):
    return a ** 3
    # return pow(a,3)
    # return a * a * a


# write a function which calculates number of steps you need to make on specified distance
# inputs: distance, length of your step
def calculate_num_step(distance_m, step_length_m):
    return int(distance_m / step_length_m)


# write a function which calculates absolute difference between numbers
# input: number1, number2
# output: result - absolute difference
def absolute_difference(number1, number2):
    if number1 > number2:
        return number1 - number2
    # solution 1
    # elif number2 > number1:
    # solution 2
    # else:
    #     return number2 - number1
    # solution 3
    return number2 - number1


def get_square_cube(num):
    square = num ** 2
    cube = num ** 3

    return square, cube

square, cube = get_square_cube(2)
