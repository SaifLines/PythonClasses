
menu = {  "Appetizers": {
                            "salads":{"Tomato Salad": 6.75, "Small Tossed Salad": 7, "Antipasto":8},
                            "Soups": {"Chiken Soup":6, "Pasta Fagioli" : 6, "lentil":6},
                            "other":{"chicken Wings":7, "Mozarella Sticks":6.75, "Pizza Fries": 5.75, "Rice Ball":2.5 }}
          
          
          
          , "Sandwiches": {
                            "Cold Sandwiches":{"Salami and Provolone": 6.5, "Ham and Provolone": 6.5},
                            "Hot Sandwiches":{"Cheese sdddteak": 8.75, "Sausage and Perppers": 7.25, "Pepper and Eggs": 6.75, "Sausage and eggs":8}
                              } }

def display_menu(menu):
    for big_section in menu:
        print(f"================================ {big_section.upper()} =============================== ")

        for small_section in menu[big_section]:
            print()
            print(f'********* {small_section} *********')

            for item in menu[big_section][small_section]:

                print(f"{item}     {menu[big_section][small_section][item]}")

        print()
        print()
    

display_menu(menu)