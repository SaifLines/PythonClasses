

menu = {  "appetizers": {
                            "salads":{"Tomato Salad": 6.75, "Small Tossed Salad": 7, "Antipasto":8},
                            "Soups": {"Chiken Soup":6, "Pasta Fagioli" : 6, "lentil":6},
                            "other":{"chicken Wings":7, "Mozarella Sticks":6.75, "Pizza Fries": 5.75, "Rice Ball":2.5 }}
          
          
          
          , "Sandwiches": {
                            "Cold Sandwiches":{"Salami and Provolone": 6.5, "Ham and Provolone": 6.5},
                            "Hot Sandwiches":{"Cheese sdddteak": 8.75, "Sausage and Perppers": 7.25, "Pepper and Eggs": 6.75, "Sausage and eggs":8}
                              } }



























def display_menu(menu):
    for section in menu:
        print(f"---------- {section.upper()} ----------")
        print()
        for subsection in menu[section]:
            print(f"*** {subsection} ***")
            for item in menu[section][subsection]:
                
                if len(item) <7:
                    print(f"{item} \t\t\t{menu[section][subsection][item]}")
                elif len(item)<15:
                    print(f"{item} \t\t{menu[section][subsection][item]}")
                else:
                    print(f"{item} \t{menu[section][subsection][item]}")
            print()
        print()
        print()

client_order={}
print("WELCOME TO OUR RESTAURANT")
display_menu(menu)

# print()
# print()
# for section in menu:
#     print(f"what kind of {section} do you want")
#     for subsection in menu[section]:
#         print(subsection)
#     subsection_answer = input("answer: ")
    
#     for item in menu[section][subsection_answer]:
#         print(item)
#     item_choice = input("I would like to order : ")
#     client_order[item_choice] = menu[section][subsection_answer][item_choice]


# print(client_order)
    






