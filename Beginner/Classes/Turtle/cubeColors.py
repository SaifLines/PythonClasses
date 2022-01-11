#CREDITS TO DONGHYUN 


import turtle as t



def cube(dimension, color1, color2, color3):
    t.speed(3)
    diagonal_dimension = dimension/2
    
    
    #first face of the cube
    t.color(color1)
    t.begin_fill()
    t.left(90)
    t.forward(dimension)
    t.right(90)
    t.forward(dimension)
    t.right(90)
    t.forward(dimension)
    t.right(90)
    t.forward(dimension)
    t.end_fill()


    t.right(135)
    t.forward(diagonal_dimension)
    t.left(45)
    t.forward(dimension)
    t.left(135)
    t.forward(diagonal_dimension)
    t.left(180)

    t.color(color2)
    t.begin_fill()
    t.forward(diagonal_dimension)
    t.right(45)
    t.forward(dimension)
    t.right(135)
    t.forward(diagonal_dimension)
    t.end_fill()

    t.color(color3)
    t.begin_fill()
    t.left(45)
    t.forward(dimension)
    t.left(135)
    t.forward(diagonal_dimension)
    t.left(45)
    t.forward(dimension)
    t.left(180)
    t.end_fill()

t.bgcolor('black')
cube(100, "lightgoldenrod", "green", "indianred1")





