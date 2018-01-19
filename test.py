'''
int1 = input("Syota luku 1: ")
int2 = input("Syota luku 2: ")
int3 = int(int1)+int(int2)

print("Luvun "+str(int1)+" ja "+str(int2)+" summa on: " +str(int3))


# Fahrenheit-konversio
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

'''

def get_numbers():
    number_csv = input("Enter your 6 digits, separated by commas: ")
    splitted_numbers = number_csv.split(",")
    return {int(number) for number in splitted_numbers}

print(get_numbers())



