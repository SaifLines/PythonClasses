import turtle




t1 = turtle.Turtle()
t1.speed(10000)
t1.color("blue")



t2 = turtle.Turtle()
t2.speed(10000)
t2.color("red")

for i in range(30):
    t2.fd(20)
    t1.fd(-20)