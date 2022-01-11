#THE PASSWORD PROGRAM

import random


#ENTER PASSWORD AND CHECK FOR STRENGTH
#returns a rating(int) (from 1 to 5) how strong is your password
# 1 point if it contains more or equal than 8 digits
# 1 point if it contains at least one small case letter
# 1 point if it contains at least one capital letter
# 1 point if it contains at least one number
# 1 point if it contains at least one sign (?.;!@#$%&*"' etc) 


def check_password_strength(password):
    points = 0
    
    capital_letter = False
    small_letter = False
    number = False
    sign = False
    
    
    if len(password) >= 8:
        print("length: " + u'\u2713')
        points += 1
    
    for letter in password:
        if letter in "abcdefghijklmnopqrstuvwxyz" and not small_letter:
            print("Small Case letter : " + u'\u2713')
            small_letter = True
            points += 1
        elif letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and not capital_letter:
            print("Capital Case letter : " + u'\u2713')
            capital_letter =True
            points += 1
        elif letter in "1234567890" and not number:
            print("number : " + u'\u2713')
            number = True
            points += 1
        elif not sign and letter in "?.;!@#$%&*\"'":
            print("sign : " + u'\u2713')
            sign=True
            points+=1
        
    return points


#INPUT LIST OF ADJ AND NOUNS
def get_input(type_of_word):
    the_list = []
    words_min = 5
    words_count = 0
    
    while words_count<words_min:
        word = input("please enter a(n) " + type_of_word + ": ")
        the_list.append(word)
        words_count += 1
        
    
    return the_list        



#GENERATE ONE PASSWORD
def generate_password(adjectives, nouns):
    
    signs = list("?.;!@#$%&*\"'")
    
    #pick a random noun
    the_noun = random.choice(nouns)
    
    #pick a random adj
    the_adj = random.choice(adjectives)
    
    #generate a random number
    the_number = random.randint(100,999)
    
    #generate a sign
    the_sign = random.choice(signs)
    
    new_password = the_adj + the_noun + str(the_number) + the_sign
    
    
    return new_password
    
#the Password: a function that wraps the whole program
# first ask the user for his ild password and check its strength
# suggest to generate another strong password for him
# how many passwords
#display the n passwords



def the_password():
    print("Welcome to the password program")
    old_password = input("your actual password: ")
    old_password_strength = check_password_strength(old_password)
    
    strength_list = [ 0 ,"very weak", "weak", "medium", "strong", "very strong"]
    print("your password is " + strength_list[old_password_strength])
    change = input("do you want us to generate a new strong password for you ?(y/n) ")
    
    if change == 'y' or change == "yes":
       
        adjectives = get_input("adjectif")
        nouns = get_input("noun")
    
        new_pass = generate_password(adjectives, nouns)
        print("your new password is " + new_pass )

        return new_pass
    
the_password()  