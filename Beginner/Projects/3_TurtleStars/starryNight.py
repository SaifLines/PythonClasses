import turtle as t
from random import randint, choice

# STARRY NIGHT
# we will have a "night theme" -> dark background color
# we are going to have multiple stars in the sky
# 4 differences between the stars: points / color / size / position
t.bgcolor("dark blue")

def star(points, color, size):
    t.speed(6000)
    t.color(color)
    t.begin_fill()
    
    for i in range(points):
        t.forward(size)
        t.right(180-(180/points))
    t.end_fill()


#we want to make an infinite loop that each time (each iteration),
# draws one star with a random color, a random size, a random points and a random position 


while True:
    #geenrade a random odd number for the variable points
    rand_points = randint(3, 6) * 2 + 1
    
    colors_list = ["red", "orange","hot pink", "pink", "seashell","white","green", "yellow", "light blue", "light green"]
    #generate a random color
    rand_color = choice(colors_list)
    
    #generate a random size (30-60)
    rand_size = randint(30,60)
    
    #generate a random position (a random x(-300,300), and a random y(-300,300) )
    rand_x= randint(-300,300)
    rand_y= randint(-300,300)

    #tell the turtle to go to the random position you generated
    t.penup()
    t.goto(rand_x, rand_y)
    t.pendown()
    
    #call the functionn star() with the  random arguments that you just generated
    
    star(rand_points, rand_color, rand_size)  
    
    
    
    
    


