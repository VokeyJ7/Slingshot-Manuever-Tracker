import numpy
import matplotlib.pyplot as plt
import numpy as np
import turtle as tr
from turtle import Turtle
####################################################################################################################
# the Spacecraft's speed has to be higher than the planet's speed for the the curve to be approximated correctly
####################################################################################################################

def pullValues(): 
    '''
    The main function for setting bounds and taking inputs
    '''
    try:
        vi=tr.textinput('Prompt 1','Entry Velocity: ')
        theta = tr.textinput('Prompt 2', 'Entry Angle: ')
        u=tr.textinput('Prompt 3',"Planet's orbital velocity: ")
        if float(vi) == 2 * float(u): 
            print("The entry speed must be more than double the planet's speed")
            exit()
        elif not ((8*float(u)*float(vi)) <= ((float(vi) - (2*float(u))) ** 2)) or (float(vi) >= (10 * float(u))):
            print("Warning: You have crossed the threshold for planetary and spacecraft velocity\nThus your velocity curve may not be approximated correctly.")
        return vi,theta,u 
    except (KeyboardInterrupt, ValueError, TypeError):
        print('Enter numeric values only.')
    

try:
    vi,theta,u=pullValues()
    theta=int(theta) 
    entrya=int(theta)
    entryv=int(vi)
    u=int(u)

  


    def velocity_curve(entry_angle, v1, U): 
        entry_angle = np.deg2rad(entry_angle) 
        return (v1 + (2*U)) * np.sqrt( 
            1 - (4*U*v1*(1 - np.cos(entry_angle))) /
            ((v1 - (2*U) ) ** 2)
        )
    

    vf = velocity_curve(theta, entryv, u) 
    print(f"Exit velocity of the spacecraft is {vf: .2f} m/s \n If speed is nan, then imaginary numbers have been approximated.")
    
    vf_x = (entryv * np.cos(np.deg2rad(theta))) + (2 * u) 
    vf_y =  entryv * np.sin(np.deg2rad(theta))
    print(f'Final velocity X component: {vf_x: .2f}, Final velocity Y component: {vf_y: .2f}') 
    
    phi=np.atan(vf_x/vf_y) 
    phi=np.rad2deg(phi)
    print(f"Exit angle is {phi: .2f} degrees.") 

    s1=tr.Screen() 
    tr.hideturtle()
    s1.setup(400,300)
    s1.bgpic('visorview.png')
    
    tr.penup()
    tr.goto(tr.xcor(),-80)
    tr.pendown()
    tr.write(f'Speed: {entryv} m/s ',align='center')


    

    def planetillust(entrya,exita,entryv,exitv,planetv): 
        try:
            
            tr.clearscreen()
            s2=tr.Screen()
            s2.setup(400,300)
            s2.bgpic("bgtest.png")

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
            
            for i in range(4):
                t3.forward(vf/100)
                t3.clone()

            tr.penup()
            tr.goto(tr.xcor(),(tr.ycor()+50))
            tr.write('Gravitational Field',align='center')

            tr.goto(100,-25)
            tr.pencolor('cyan')
            tr.write(f'Entry angle {entrya: .2f}°\nEntry speed: {entryv: .2f}',align='center') # writing the velocity information

            tr.goto(100, 40)
            tr.write(f'Exit angle {exita: .2f}°\nExit speed: {exitv: .2f}', align='center')

            tr.up()
            tr.goto(0,10)
            tr.pensize(1)
            
            for i in range(4):
                tr.tiltangle(0)
                tr.forward(u/100)
                tr.down()
                tr.circle(10)
                tr.up()

            tr.done()

            
        except (KeyboardInterrupt, tr.Terminator, tr.TurtleGraphicsError):
            print('Turtle Animation terminated.')


    try: 
        start = input('continue? ')
        if start.lower().replace(" ",'') == 'y':
            planetillust(entrya,exita=phi,entryv=entryv,exitv=vf,planetv=u)
        elif start.lower().replace(" ",'') == 'n':
            exit()
        else:
            print('Type only y or n.')
    except(KeyboardInterrupt, ValueError, TypeError):
        print('Type only y or n.')


   
    x = np.linspace(150,500, 500)
    y = velocity_curve(x, entryv, u)

    plt.plot(x, y, color="Green", linestyle="-.", marker="o", label="Velocity Curve") 
    plt.legend()
    plt.title('velocity change based on angle change')
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.savefig('Plot1.png')
    plt.show()

    with open('lastSimData.txt', "w") as file: 
        file.write(f'Entry Velocity: {entryv: .2f} m/s\n'
                   f'Entry Angle: {entrya: .2f} deg\n'
                   f'Planet Velocity: {u: .2f} m/s\n'
                   f'\nExit Velocity: {vf: .2f} m/s\n'
                   f'Vector form = {vf_x: .2f}i + {vf_y: .2f}j\n'
                   f'Exit angle: {phi: .2f} deg')


except (KeyboardInterrupt, ValueError, TypeError, FileExistsError, FileNotFoundError): 
        print('Enter numeric values only.')