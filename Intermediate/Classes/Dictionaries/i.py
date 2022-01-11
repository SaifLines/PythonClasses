menu = {  "appetizers": {
                        "salads":{"Tomato Salad": 6.75, "Small Tossed Salad": 7, "Antipasto":8},
                        "soups": {"Chiken Soup":6, "Pasta Fagioli" : 6, "lentil":6},
                        "other":{"chicken Wings":7, "Mozarella Sticks":6.75, "Pizza Fries": 5.75, "Rice Ball":2.5 }}
          
          
          
        , "Sandwiches": {
                        "Cold Sandwiches":{"Salami and Provolone": 6.5, "Ham and Provolone": 6.5},
                        "Hot Sandwiches":{"Cheese steak": 8.75, "Sausage and Perppers": 7.25, "Pepper and Eggs": 6.75, "Sausage and eggs":8}
                        } }

print("-----------------MENU-----------------")
print('APPETIZERS')
print(f" SALADS {menu['appetizers']['salads']}")
print(" SOUPS " + str(menu['appetizers']['soups']))
print(" OTHER " + str(menu['appetizers']['other']))
print()
print('SANDWICHES')
print("HOT SANDWICHES " + str(menu['Sandwiches']['Cold Sandwiches']))
print("COLD SANDWICHES " + str(menu['Sandwiches']['Hot Sandwiches']))

print()

order1 = input('Please order an appetizer (salads/soups/other):')
if order1 == 'salads':
    appetizer = input ('Please choose a salad: ')
elif order1 == 'soups':
    appetizer = input ('Please choose a soup: ')
else:
    appetizer = input ('Please choose other thing: ')
    
print()

order2 = input('Please order a sandwich (Cold Sandwiches/Hot Sandwiches): ')
if order2 == 'Cold Sandwiches':
    sand = input ('Please choose a cold sandwich: ')
else:
    sand = input ('Please choose a hot sandwich: ')

price = menu['appetizers'][order1][appetizer] + menu['Sandwiches'][order2][sand]

cheese = input('Do you want extra cheese($1.00)? (y/n): ')

if cheese == 'y':
    price = price + 1
else:
    price = price
    
print()
print("-------------RECEIPT-------------")
print("your order: ")
print(appetizer + " : " + str(menu['appetizers'][order1][appetizer]))
print(sand + " : " + str(menu['Sandwiches'][order2][sand]))
print('your total price is ' + str(price) + '.')


