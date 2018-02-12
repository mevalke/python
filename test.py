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




import sys

def k_menu():
    print("Komioita kenkiä paikat pullollansa")
    valinta = input("1. Paavalikko, q. Lopeta: ")
    while True:
        if valinta == '1':
            p_menu()
        elif valinta == 'q':
            sys.exit(0)
        else:
            print("Valitse 1 tai q!")
        valinta = input("1. Paavalikko, q. Lopeta")

def t_menu():
    print("Komioita takkeja paikat pullollansa")
    valinta = input("1. Paavalikko, q. Lopeta: ")
    while True:
        if valinta == '1':
            p_menu()
        elif valinta == 'q':
            sys.exit(0)
        else:
            print("Valitse 1 tai q!")
        valinta = input("1. Paavalikko, q. Lopeta")

def p_menu():
    print("Mista olet kiinnostunut oi asiakas?")
    valinta = input("1. Kengat, 2. Takit, 3. Housut, q. Lopeta: ")
    while True:
        if valinta == '1':
            k_menu()
        if valinta == '2':
            t_menu()
        elif valinta == 'q':
            sys.exit(0)
        else:
            print("Valitse 1,2,3 tai q!")
            valinta = input("1. Kengat, 2. Takit, 3. Housut, q. Lopeta: ")

p_menu()



# list-koulutehtäviä
# Tulostaa listan suurimman luvun:
a = 1
the_list = [ 1,2,4,3]
for i in the_list:
    if i > a:
        a = i
print(a)

# Kääntää listan, tässä käytetään instertiä hommaa helpottamaan:
old_list = [1,2,3,4,5]
new_list = []

for i in old_list:
    new_list.insert(0, i)
print(new_list)

new_list = []

# Oma toteutus reversestä, jossa ei käytetä valmiita methodeja
prompt_for_list = input("Type the list content: ")
the_list = list(prompt_for_list)
the_len = len(the_list)

while the_len != 0:
    new_list.append(the_list[-1:])
    del the_list[-1]
    the_len = the_len - 1

print(new_list)



# Funktio, joka tarkistaa onko alkio listassa.
#
list_to_check = [2,3,4]
def my_funcion(my_param):
    for i in list_to_check:
        if i == my_param:
            return True

my_prompt = input("Type a number: ")

while my_prompt != 'q':
    my_prompt = int(my_prompt)
    if my_funcion(my_prompt):
        print("Found!")
    else:
        print("Not found!")
    my_prompt = input("Type a number: ")



# Tulosta listan joka toinen alkio
my_list = [6,7,8,9,10,11,12]

for i,j in enumerate(my_list):
    i = 1
    if j % 2 == 0:
        print(j)

# Laske alkioiden summa
my_list = [2,3,4]
j = 0
for i in my_list:
    j = j + i

print(j)

# Edellinen fiksummin
my_list = [1,2,3,4,5,6]

print(my_list[::2])


# Tarkista, onko string palindromi
def process_len(list_param):
    if len(list_param) % 2 != 0:                # Jos listan pituus on pariton
        to_even = len(list_param) - 1           # vähennetään 1
        return to_even / 2                      # ja palautetaan puolikas jäljellejäävästä
    else:
        return len(list_param) / 2              # Jos pituus on valmiiksi parillinen, jaetaan suoraan kahdella

def extract_list_1(list_param, len_param):
    return list_param[0:len_param]

def extract_list_2(list_param, len_param):
    list_to_return = list_param[-len_param:]    # Huom! esim. viimeiset kaksi elementtiä list[-2:] https://stackoverflow.com/questions/646644/how-to-get-last-items-of-a-list-in-python/647299
    list_to_return.reverse()                    # HUOM! new_list = list_to_return.reverse() --> ei toimi
    return list_to_return                       # HUOM! return list_to_return.reverse() --> ei toimi

my_prompt = input("Type string: ")
prompt_as_list = list(my_prompt)
halfway = int(process_len(prompt_as_list))

# Debugging
# print(halfway)
# print(str(extract_list_1(prompt_as_list,halfway)))
# print(str(extract_list_2(prompt_as_list,halfway)))

if extract_list_1(prompt_as_list,halfway) == extract_list_2(prompt_as_list,halfway):
    print("On palindromi!")
else:
    print("Ei ole palindromi!")


# "sum" for loopilla
my_list = input("Type the numbers: ")
result = 0
splitted_list = my_list.split(",")
numbers_as_int = []

for i in splitted_list:
    numbers_as_int.append(int(i))

for i in numbers_as_int:
#    print(result)
    result = result + i

print("Result {}".format(result))



# "sum" while loopilla
temp_list = input("Type the numbers: ")
splitted_list = temp_list.split(",")
list_as_int = []
list_len = len(splitted_list)
result = 0
i = 0

while i != list_len:
    list_as_int.append(int(splitted_list[i]))
    i = i +1


i = 0

while i != list_len:
    result = result + list_as_int[i]
    i = i + 1

print(result)


# shift
shift = input("How many chars to shift? ")
shift = int(shift)

my_list = [1,2,3,4,5,6]

to_be_added = []

for i in my_list[:shift]:
    to_be_added.append(i)

for i in to_be_added:
    my_list.append(i)

del my_list[:shift]

print(my_list)

# Tehtävä 14: https://sites.google.com/site/vaoohjelmointi/home/harjoitukset-ii
# Tulostetaan funktion argumentit kehykseen
def kyltintekija(*args):
    mitta = int(0)
    for i in args:
        if len(i) > mitta:
            mitta = len(i)
    mitta = mitta+2
    print('*' * mitta)
    for i in args:
        x = ' '
        spaces = mitta - len(i) - 2
        print('*'+i+(spaces*x)+'*')
    print('*' * mitta)

kyltintekija('foo','bar','bazooka', 'foobarbazspam')

ascii dance:

import time
def kadetylos():
    print('\n'*30)
    print('\o/')
    print(' |')
    print('/ \\')
    time.sleep(1)
def kadetsivulle():
    print('\n'*30)
    print('_o_')
    print(' |')
    print('/ \\')
    time.sleep(1)
def kadetalas():
    print('\n'*30)
    print(' o')
    print('/|\\')
    print('/ \\')
    time.sleep(1)
def sivuprofiilioikea():
    print('\n'*30)
    print(' o/')
    print(' |')
    print(' |\\')
    time.sleep(1)
def sivuprofiilivasen():
    print('\n'*30)
    print('\o')
    print(' |')
    print('/|')
    time.sleep(1)

while True:
    kadetylos()
    kadetsivulle()
    kadetalas()
    sivuprofiilioikea()
    sivuprofiilivasen()

"""

