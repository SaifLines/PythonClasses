import turtle as t
import random

def random_stars(points,size,color):  
    t.bgcolor('midnightblue')

    t.color(color)
    t.begin_fill()
    for i in range(points):
        t.fd(size)
        t.left(180-(180/points))
    t.end_fill()
   
yellow_list = ['darkgoldenrod1','gold1','lightgoldenrod1','khaki2','yellow','darksalmon','powderblue']
blue_list = ['darkslategray1','aquamarine1','deepskyblue','darkseagreen1','powderblue']
red_list = ['brown1','coral','pink','mistyrose1','salmon','peachpuff']
purple_list = ['darkorchid1','lavender','lightpink','mediumpurple1','thistle1']

'''
colors = input('What color do you want your stars to be?(yellow/blue/red/violet): ')
if colors == 'yellow':
    colors = yellow_list
elif colors == 'blue':
    colors = blue_list
elif colors == 'red':
    colors = red_list
elif colors == 'violet':
    colors = purple_list
else:
    print('error')
    colors = yellow_list
'''
#draw the two central lines (axis)
t.bgcolor("darkblue")
t.pensize(5)
t.penup()
t.goto(-1000,0)
t.pendown()
t.color("white")
t.fd(2000)
t.penup()
t.goto(0,500)
t.right(90)
t.pendown()
t.forward(1000)
t.pensize(1)


#YELLOW LIST
colors = yellow_list
speed = 1000
for i in range(150):
    t.speed(speed)
    t.penup()
    x = random.randint(-800,-50)
    y = random.randint(50,500)
    t.goto(x,y)
    t.pendown()
    point = random.randint(2,6)
    points = point*2+1
    size = random.randint(30,70)
    color = random.choice(colors)
    random_stars(points,size,color)



#BLUE LIST
colors = blue_list
speed = 1000
for i in range(150):
    t.speed(speed)
    t.penup()
    x = random.randint(50,800)
    y = random.randint(50,500)
    t.goto(x,y)
    t.pendown()
    point = random.randint(2,6)
    points = point*2+1
    size = random.randint(30,70)
    color = random.choice(colors)
    random_stars(points,size,color)
    
    
#RED LIST
colors = red_list
speed = 1000
for i in range(150):
    t.speed(speed)
    t.penup()
    x = random.randint(-800,-50)
    y = random.randint(-400,-50)
    t.goto(x,y)
    t.pendown()
    point = random.randint(2,6)
    points = point*2+1
    size = random.randint(30,70)
    color = random.choice(colors)
    random_stars(points,size,color)
    
    
#PURPLE LIST
colors = purple_list
speed = 1000
for i in range(150):
    t.speed(speed)
    t.penup()
    x = random.randint(50,800)
    y = random.randint(-400,-50)
    t.goto(x,y)
    t.pendown()
    point = random.randint(2,6)
    points = point*2+1
    size = random.randint(30,70)
    color = random.choice(colors)
    random_stars(points,size,color)