# coding=utf-8
"""
int1 = input("Syota luku 1: ")
int2 = input("Syota luku 2: ")
int3 = int(int1)+int(int2)

print("Luvun "+str(int1)+" ja "+str(int2)+" summa on: " +str(int3))


# Fahrenheit-konversio (round tekee pyöristyksen)
temperature = input("Type the temperature: ")
conversion = round(int(temperature)*9/5+32)

print("Temperature in Fahrenheit: "+str(conversion))



age = input("Provide age: ")
size = input("Provide size: ")

print("You are {myage} years old and have the {mysize} shoe size".format(myage=age,mysize=size))


import random
min_int = 100

for i in range(100):
    rand_int = random.randint(0,100)
    if rand_int <= min_int:
        min_int = rand_int
        print("Minimium number is now set to: {}".format(min_int))
print("The final minimal number is: "+ str(min_int))


import random
magic_numbers = [ random.randint(0, 9), random.randint(0, 9) ]

def prompt_user():
    number_var = input("Try to guess the magic number: ")
    if int(number_var) in magic_numbers:
        return "You guessed it!"
    else:
        return "You didn´t guess it"

def the_loop(attempts):
    for i in range(attempts):
        print(prompt_user())

user_attempts = int(input("How many times to loop: "))
the_loop(user_attempts)

print("These are the magic numbers: {}".format(magic_numbers))


def my_method(input_number, divisor):
    if divisor == 0:
        return None
    return input_number / divisor
print(my_method(8000,0))


my_numbers = "1, 2, 3, 4, 5"
splitted_numbers = my_numbers.split(",")
print(splitted_numbers)
splitted_numbers_as_int = []
for i in splitted_numbers:
    splitted_numbers_as_int.append(int(i))
print(splitted_numbers_as_int)

my_numbers = "1, 2, 3, 4, 5"
splitted_numbers = my_numbers.split(",")
print([int(number) for number in splitted_numbers])

set_1 = {1,2,3,4,}
set_2 = {3,4,5,6}
print(set_1.intersection(set_2))

import random

def menu():
    user_numbers = get_numbers()
    random_numbers = create_lottery_numbers()
    matched_numbers = user_numbers.intersection(random_numbers)
    print("The winning numbers are: {}, you won {}".format(matched_numbers, 100 ** len(matched_numbers)))

def get_numbers():
    number_csv = input("Enter your 6 digits, separated by commas: ")
    splitted_numbers = number_csv.split(",")
    return {int(number) for number in splitted_numbers}

def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1,20))
    return values

print(menu())


dict_for_fun = { "my_name": "Miikka", "Age": 44 }
print(dict_for_fun["my_name"])



user_feed = input("Type three numbers: ")
feed_transformed = [ str(i) for i in str(user_feed) ]
my_var = ''

for i in feed_transformed:
    if i == '1':
        my_var = my_var+'one '
    elif i == '2':
        my_var = my_var+'two '
    elif i == '3':
        my_var = my_var+'three '

print(my_var)



def my_calculation():
    temperature = input("Type the temperature: ")
    conversion = round(int(temperature)*9/5+32)

    print("Temperature in Fahrenheit: "+str(conversion))

def my_prompt():
    answer = input("Do you want to run my_calculation: ")
    if answer == "y":
        return True
    elif answer == "n":
        return False

while my_prompt():
    my_calculation()

def add_user():
    var_name = input("Type the name: ")
    var_user = {
        'name': var_name,
        'marks': []
    }
    return var_user

def append_mark(student, var_marks):
    student['marks'].append(var_marks)

def calculate_avg(student):
    var_len_marks = len(student['marks'])
    if var_len_marks == 0:
        return 0
    var_sum_marks = sum(student['marks'])
    return var_sum_marks / var_len_marks

s = add_user()
print(calculate_avg(s))

append_mark(s,5)
print(calculate_avg(s))

"""

student_list = []

def create_student():
    student_name = input("Type student name: ")
    student_data = {
        'name': student_name,
        'marks': []
    }
    return student_data

def add_mark(student, mark):
    student['marks'].append(mark)

def print_student_list():
    for i, student in enumerate(student_list):
        print("ID: {}, Name: {}, Marks: {}".format(i, student['name'],student['marks']))

def modify_student():
    s = create_student()
    get_mark = input("Type the mark you wish to add: ")
    add_mark(s, get_mark)
    student_list.append(s)

def menu():
    answer = input("Please select an option, c - Create new user, a - Append mark, p - Print student list, q - Quit: ")
    while answer != 'q':
        if answer == 'c':
            create_student()
        elif answer == 'a':
            add_mark()
        elif answer == 'p':
            print_student_list()
        answer = input("Please select an option, c - Create new user, a - Append mark, p - Print student list, q - Quit: ")

menu()