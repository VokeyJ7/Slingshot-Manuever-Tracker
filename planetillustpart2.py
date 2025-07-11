import turtle as tr
from random import randint
from PIL import Image

# img = Image.open('visorview.jpg')

# img.save('visorview.png')

entrya=randint(1,89)
print(entrya)
exita=randint(1,89)

def planetillust(entrya,exita):
    s2=tr.Screen()
    s2.setup(400,300)
    s2.bgpic('visorview.png')

    tr.pensize(5)
    tr.speed(0)

    tr.pu()
    tr.goto(0,-30)
    tr.pd()
    tr.circle(50)
    tr.hideturtle()

    t2=tr.Turtle()
    t2.pensize(5)
    t2.pencolor('cyan')
    t2.hideturtle()
    t2.up()
    t2.goto(tr.xcor(),tr.ycor())
    t2.down()
    t2.right(entrya)
    t2.forward(200)

    t3=tr.Turtle()
    t3.up()
    t3.pensize(5)
    t3.pencolor('cyan')
    t3.goto(tr.xcor(),(tr.ycor()+100))
    t3.down()
    t3.left(exita)
    t3.forward(200)

    tr.penup()
    tr.goto(tr.xcor(),(tr.ycor()+50))
    tr.write('Gravitational Field',align='center')

    tr.done()


planetillust(entrya,exita)
