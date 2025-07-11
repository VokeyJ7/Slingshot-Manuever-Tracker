import turtle as tr
from turtle import Turtle

def pullValues():
    vi=tr.textinput('Prompt 1','Entry Velocity: ')
    theta = tr.textinput('Prompt 2', 'Entry Angle: ')
    u=tr.textinput('Prompt 3',"Planet's orbital velocity: ")
    return vi,theta,u

def part1exec():
    vi,theta,u=pullValues()

    s1=tr.Screen()
    tr.hideturtle()
    s1.setup(400,300)
    s1.bgpic("bgtest.png")
    tr.penup()
    tr.goto(tr.xcor(),-80)
    tr.pendown()
    tr.write('Speed: ',align='center')
    s1.exitonclick()
    tr.done()

pullValues()
part1exec()

