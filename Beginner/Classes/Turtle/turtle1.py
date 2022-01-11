import turtle as t
#import everything (every function and method) from the turtle module


#created an object turtle adn assigned it to a variable t



#rectangle
'''
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
'''

#make a function called draw_rectangle(width,height,color)
#rectangle with a for loop



def draw_rectangle(width, height, the_color):
    t.hideturtle()
    t.begin_fill()
    t.color(the_color)
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


draw_rectangle(200,50,"red")
#arc
'''
for counter in range(100):
    t.forward(1)
    t.left(1)
'''
