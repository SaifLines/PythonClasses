

# input of a function = argument = paramter 
def functionnnnnn():
    print("hello world")
    print("this is a good day")
    


#Create a function with one argument call it name,
#and f(name) is going to print hello name and then return hello name


def print_name(name):
    print("hello "+ name)
    return "hi" + name

x = print_name("Seif")
print(x)

def greetings():
    print("hello")
    print("welcome")
    print("good morning")



#Seconds functions

'''
def print_seconds_per_day():
    hours =24
    minutes = 24*60
    seconds = minutes *60
    print(seconds)

print_seconds_per_day()
'''

#do some modifications on teh print_seconds_per_Day() function
# the function is going to take one argument/input which is the number of days
#rather than printing we are going to return the number of seconds per specified days
#(that we passed through the argument)
#edit the function name so it corresponds to the new use of the function


def seconds_per_days(days):
    hours =24
    minutes = 24*60
    seconds = minutes *60 #the number of seconds in one day
    seconds_per_days = seconds*days #the number of seconds in days
    return seconds_per_days

def f(x):
    z= x*x
    return z


#number_of_days = int(input("days: "))

#print('There are ' + str(seconds_per_days(number_of_days)) + ' seconds in ' + str(number_of_days) + ' day(s).') 
