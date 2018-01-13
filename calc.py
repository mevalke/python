age = input('Enter your age: ')
seconds = int(age) * 365 * 24 * 60 * 60

# print('The number of seconds in '+str(age)+' years: '+str(seconds))
print('The number of seconds in {} years: {}'.format(age,int(seconds)))