

fav_food = {"Iaan": {"dish" : "Pasta", "drink":"Cider"},
            "Hyerin": { "dish": "pizza", "drink":"nestea"},
            "Seif": {"dish":"French Fries","drink":"Coffee"}
            }




#"Iaan's favourite dish is Pasta and favourite drink is Cider"

#print(fav_food["Iaan"]["dish"])

for name in fav_food:
    #print(name + "'s favourite dish is " + fav_food[name]["dish"] + " and favourite drink is "+ fav_food[name]["drink"] + "." )
    
    print(f"{name}'s favourite dish is {fav_food[name]['dish']} and favourite drink is {fav_food[name]['drink']}.")



