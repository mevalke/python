'''
int1 = input("Syota luku 1: ")
int2 = input("Syota luku 2: ")
int3 = int(int1)+int(int2)

print("Luvun "+str(int1)+" ja "+str(int2)+" summa on: " +str(int3))


# Fahrenheit-konversio
temperature = input("Type the temperature: ")
conversion = round(int(temperature)*9/5+32)

print("Temperature in Fahrenheit: "+str(conversion))

'''

age = input("Provide age: ")
size = input("Provide size: ")

print("You are {myage} years old and have the {mysize} shoe size".format(myage=age,mysize=size))

