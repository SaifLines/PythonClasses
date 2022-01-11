



    

fruits_list = [ "Kiwi", "Melon", "Banana", "Strawberry", "Watermelon", "Mango", "Peach" ]

#loop through the list using an integer loop variable i
#each iteration we are going to compare the element of index i with the word that we are looking for ("strawberry)
# print i (we found the index of the element we are looking for)

'''
for i in range(0,len(fruits_list)):
    if fruits_list[i] == "Strawberry":
        print("yaaay we found teh index of strawberry : " + str(i))
'''
'''
ticket = input("do u have a ticket: ")

while ticket == 'n' or ticket != 'y':
    print("you don't have tickets then you don't enter")
    ticket = input("do u have a ticket: ")

print('great u have a ticket! u can enter')
'''

real_password = "pass1234"
# we are going to ask the user to put a password
# if the input password matches with the real password then print "access granted"
# if the input password do not match the real password print "access denied" and we let the user type a new password  


input_password = input("password: ")
while input_password != real_password:
    print("access denied. Try again")
    input_password = input("password: ")

print("access granted ")
