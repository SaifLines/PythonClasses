

fav_food = {"Yeonhu": ["SUSHIIIIIII","bubble tea"], "Eugene": {"main dish":"rice", "drink":"milk", "desert":"iceream"},
            "Kee":"Pizza", "Sunjae":"pizza", "Yejin":"Noodle"}

#name = input("name: ")


for name in fav_food:
    
    if name== "Eugene":
        continue
    
    print( name + "'s favroite food is " + str(fav_food[name]))
    
    #another way of doing it 
    #print(f"{name}'s favorite food is {fav_food[name]}")



