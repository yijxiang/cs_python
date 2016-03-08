# -*- coding: utf-8 -*-
"""
***********************************************
Pablo Fernandez 
Emily Klein
Copyright 2016, www.pablofernandez.com
***********************************************
"""

print("************************************");
print("Pablo Fernandez");
print("Emily Klein");
print("Program 05 Herd of Turtles");
print("A&B:");
print("************************************");

"""
Above and Beyond
- Not written yet
"""

import turtle 
import math   
import random

turtles =[]

n = 99999
while((n>20) | (n<1)):
    n = int(input("How many turtles would you like (1-20):  "))

turtle_1 = turtle.Turtle()
turtle_2 = turtle.Turtle()
turtle_3 = turtle.Turtle()
turtle_4 = turtle.Turtle()
turtle_5 = turtle.Turtle()
turtle_6 = turtle.Turtle()
turtle_7 = turtle.Turtle()
turtle_8 = turtle.Turtle()
turtle_9 = turtle.Turtle()
turtle_10 = turtle.Turtle()
turtle_11 = turtle.Turtle()
turtle_12 = turtle.Turtle()
turtle_13 = turtle.Turtle()
turtle_14 = turtle.Turtle()
turtle_15 = turtle.Turtle()
turtle_16 = turtle.Turtle()
turtle_17 = turtle.Turtle()
turtle_18 = turtle.Turtle()
turtle_19 = turtle.Turtle()
turtle_20 = turtle.Turtle()

turtle_status = {
    turtle_1: 'Sleeping',
    turtle_2: 'Sleeping',
    turtle_3: 'Sleeping',
    turtle_4: 'Sleeping',
    turtle_5: 'Sleeping',
    turtle_6: 'Sleeping',
    turtle_7: 'Sleeping',
    turtle_8: 'Sleeping',
    turtle_9: 'Sleeping',
    turtle_10: 'Sleeping',
    turtle_11: 'Sleeping',
    turtle_12: 'Sleeping',
    turtle_13: 'Sleeping',
    turtle_14: 'Sleeping',
    turtle_15: 'Sleeping',
    turtle_16: 'Sleeping',
    turtle_17: 'Sleeping',
    turtle_18: 'Sleeping',
    turtle_19: 'Sleeping',
    turtle_20: 'Sleeping'
}

turtle_colors = {
    turtle_1: "#%03x" % random.randint(0, 0xFFF),
    turtle_2: "#%03x" % random.randint(0, 0xFFF),
    turtle_3: "#%03x" % random.randint(0, 0xFFF),
    turtle_4: "#%03x" % random.randint(0, 0xFFF),
    turtle_5: "#%03x" % random.randint(0, 0xFFF),
    turtle_6: "#%03x" % random.randint(0, 0xFFF),
    turtle_7: "#%03x" % random.randint(0, 0xFFF),
    turtle_8: "#%03x" % random.randint(0, 0xFFF),
    turtle_9: "#%03x" % random.randint(0, 0xFFF),
    turtle_10: "#%03x" % random.randint(0, 0xFFF),
    turtle_11: "#%03x" % random.randint(0, 0xFFF),
    turtle_12: "#%03x" % random.randint(0, 0xFFF),
    turtle_13: "#%03x" % random.randint(0, 0xFFF),
    turtle_14: "#%03x" % random.randint(0, 0xFFF),
    turtle_15: "#%03x" % random.randint(0, 0xFFF),
    turtle_16: "#%03x" % random.randint(0, 0xFFF),
    turtle_17: "#%03x" % random.randint(0, 0xFFF),
    turtle_18: "#%03x" % random.randint(0, 0xFFF),
    turtle_19: "#%03x" % random.randint(0, 0xFFF),
    turtle_20: "#%03x" % random.randint(0, 0xFFF)
}

turtle_position_x = {
    turtle_1: random.randrange(-400, 400),
    turtle_2: random.randrange(-400, 400),
    turtle_3: random.randrange(-400, 400),
    turtle_4: random.randrange(-400, 400),
    turtle_5: random.randrange(-400, 400),
    turtle_6: random.randrange(-400, 400),
    turtle_7: random.randrange(-400, 400),
    turtle_8: random.randrange(-400, 400),
    turtle_9: random.randrange(-400, 400),
    turtle_10: random.randrange(-400, 400),
    turtle_11: random.randrange(-400, 400),
    turtle_12: random.randrange(-400, 400),
    turtle_13: random.randrange(-400, 400),
    turtle_14: random.randrange(-400, 400),
    turtle_15: random.randrange(-400, 400),
    turtle_16: random.randrange(-400, 400),
    turtle_17: random.randrange(-400, 400),
    turtle_18: random.randrange(-400, 400),
    turtle_19: random.randrange(-400, 400),
    turtle_20: random.randrange(-400, 400)
}

turtle_position_y = {
    turtle_1: random.randrange(-400, 400),
    turtle_2: random.randrange(-400, 400),
    turtle_3: random.randrange(-400, 400),
    turtle_4: random.randrange(-400, 400),
    turtle_5: random.randrange(-400, 400),
    turtle_6: random.randrange(-400, 400),
    turtle_7: random.randrange(-400, 400),
    turtle_8: random.randrange(-400, 400),
    turtle_9: random.randrange(-400, 400),
    turtle_10: random.randrange(-400, 400),
    turtle_11: random.randrange(-400, 400),
    turtle_12: random.randrange(-400, 400),
    turtle_13: random.randrange(-400, 400),
    turtle_14: random.randrange(-400, 400),
    turtle_15: random.randrange(-400, 400),
    turtle_16: random.randrange(-400, 400),
    turtle_17: random.randrange(-400, 400),
    turtle_18: random.randrange(-400, 400),
    turtle_19: random.randrange(-400, 400),
    turtle_20: random.randrange(-400, 400)
}

"""
Code Note
The following code is necessary because since each Turtle is tracked by multiple 
dictionary data structures holding the status of the turtle, color of the turtle, 
positions of the turtle, this is currenty the best method since a for loop is going
to be going through the Awake turtles and then accessing colors and other necessary
information. 
"""

if(n==1):
    turtles = [turtle_1]
    turtle_status[turtle_1] = "Awake"
    
if(n==2):
    turtles = [turtle_1, turtle_2]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"

if(n==3):
    turtles = [turtle_1, turtle_2, turtle_3]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"

if(n==4):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"

if(n==5):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"

if(n==6):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"
    turtle_status[turtle_6] = "Awake"

if(n==7):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"
    turtle_status[turtle_6] = "Awake"
    turtle_status[turtle_7] = "Awake"

if(n==8):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7, turtle_8]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"
    turtle_status[turtle_6] = "Awake"
    turtle_status[turtle_7] = "Awake"
    turtle_status[turtle_8] = "Awake"

if(n==9):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7, turtle_8, turtle_9]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"
    turtle_status[turtle_6] = "Awake"
    turtle_status[turtle_7] = "Awake"
    turtle_status[turtle_8] = "Awake"
    turtle_status[turtle_9] = "Awake"

if(n==10):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7, turtle_8, turtle_9, turtle_10]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"
    turtle_status[turtle_6] = "Awake"
    turtle_status[turtle_7] = "Awake"
    turtle_status[turtle_8] = "Awake"
    turtle_status[turtle_9] = "Awake"
    turtle_status[turtle_10] = "Awake"

if(n==11):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7, turtle_8, turtle_9, turtle_10, turtle_11]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"
    turtle_status[turtle_6] = "Awake"
    turtle_status[turtle_7] = "Awake"
    turtle_status[turtle_8] = "Awake"
    turtle_status[turtle_9] = "Awake"
    turtle_status[turtle_10] = "Awake"
    turtle_status[turtle_11] = "Awake"

if(n==12):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7, turtle_8, turtle_9, turtle_10, turtle_11, turtle_12]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"
    turtle_status[turtle_6] = "Awake"
    turtle_status[turtle_7] = "Awake"
    turtle_status[turtle_8] = "Awake"
    turtle_status[turtle_9] = "Awake"
    turtle_status[turtle_10] = "Awake"
    turtle_status[turtle_11] = "Awake"
    turtle_status[turtle_12] = "Awake"

if(n==13):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7, turtle_8, turtle_9, turtle_10, turtle_11, turtle_12, turtle_13]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"
    turtle_status[turtle_6] = "Awake"
    turtle_status[turtle_7] = "Awake"
    turtle_status[turtle_8] = "Awake"
    turtle_status[turtle_9] = "Awake"
    turtle_status[turtle_10] = "Awake"
    turtle_status[turtle_11] = "Awake"
    turtle_status[turtle_12] = "Awake"
    turtle_status[turtle_13] = "Awake"

if(n==14):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7, turtle_8, turtle_9, turtle_10, turtle_11, turtle_12, turtle_13, turtle_14]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"
    turtle_status[turtle_6] = "Awake"
    turtle_status[turtle_7] = "Awake"
    turtle_status[turtle_8] = "Awake"
    turtle_status[turtle_9] = "Awake"
    turtle_status[turtle_10] = "Awake"
    turtle_status[turtle_11] = "Awake"
    turtle_status[turtle_12] = "Awake"
    turtle_status[turtle_13] = "Awake"
    turtle_status[turtle_14] = "Awake"

if(n==15):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7, turtle_8, turtle_9, turtle_10, turtle_11, turtle_12, turtle_13, turtle_14, turtle_15]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"
    turtle_status[turtle_6] = "Awake"
    turtle_status[turtle_7] = "Awake"
    turtle_status[turtle_8] = "Awake"
    turtle_status[turtle_9] = "Awake"
    turtle_status[turtle_10] = "Awake"
    turtle_status[turtle_11] = "Awake"
    turtle_status[turtle_12] = "Awake"
    turtle_status[turtle_13] = "Awake"
    turtle_status[turtle_14] = "Awake"
    turtle_status[turtle_15] = "Awake"

if(n==16):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7, turtle_8, turtle_9, turtle_10, turtle_11, turtle_12, turtle_13, turtle_14, turtle_15, turtle_16]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"
    turtle_status[turtle_6] = "Awake"
    turtle_status[turtle_7] = "Awake"
    turtle_status[turtle_8] = "Awake"
    turtle_status[turtle_9] = "Awake"
    turtle_status[turtle_10] = "Awake"
    turtle_status[turtle_11] = "Awake"
    turtle_status[turtle_12] = "Awake"
    turtle_status[turtle_13] = "Awake"
    turtle_status[turtle_14] = "Awake"
    turtle_status[turtle_15] = "Awake"
    turtle_status[turtle_16] = "Awake"

if(n==17):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7, turtle_8, turtle_9, turtle_10, turtle_11, turtle_12, turtle_13, turtle_14, turtle_15, turtle_16, turtle_17]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"
    turtle_status[turtle_6] = "Awake"
    turtle_status[turtle_7] = "Awake"
    turtle_status[turtle_8] = "Awake"
    turtle_status[turtle_9] = "Awake"
    turtle_status[turtle_10] = "Awake"
    turtle_status[turtle_11] = "Awake"
    turtle_status[turtle_12] = "Awake"
    turtle_status[turtle_13] = "Awake"
    turtle_status[turtle_14] = "Awake"
    turtle_status[turtle_15] = "Awake"
    turtle_status[turtle_16] = "Awake"
    turtle_status[turtle_17] = "Awake"

if(n==18):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7, turtle_8, turtle_9, turtle_10, turtle_11, turtle_12, turtle_13, turtle_14, turtle_15, turtle_16, turtle_17, turtle_18]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"
    turtle_status[turtle_6] = "Awake"
    turtle_status[turtle_7] = "Awake"
    turtle_status[turtle_8] = "Awake"
    turtle_status[turtle_9] = "Awake"
    turtle_status[turtle_10] = "Awake"
    turtle_status[turtle_11] = "Awake"
    turtle_status[turtle_12] = "Awake"
    turtle_status[turtle_13] = "Awake"
    turtle_status[turtle_14] = "Awake"
    turtle_status[turtle_15] = "Awake"
    turtle_status[turtle_16] = "Awake"
    turtle_status[turtle_17] = "Awake"
    turtle_status[turtle_18] = "Awake"

if(n==19):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7, turtle_8, turtle_9, turtle_10, turtle_11, turtle_12, turtle_13, turtle_14, turtle_15, turtle_16, turtle_17, turtle_18, turtle_19]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"
    turtle_status[turtle_6] = "Awake"
    turtle_status[turtle_7] = "Awake"
    turtle_status[turtle_8] = "Awake"
    turtle_status[turtle_9] = "Awake"
    turtle_status[turtle_10] = "Awake"
    turtle_status[turtle_11] = "Awake"
    turtle_status[turtle_12] = "Awake"
    turtle_status[turtle_13] = "Awake"
    turtle_status[turtle_14] = "Awake"
    turtle_status[turtle_15] = "Awake"
    turtle_status[turtle_16] = "Awake"
    turtle_status[turtle_17] = "Awake"
    turtle_status[turtle_18] = "Awake"
    turtle_status[turtle_19] = "Awake"

if(n==20):
    turtles = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6, turtle_7, turtle_8, turtle_9, turtle_10, turtle_11, turtle_12, turtle_13, turtle_14, turtle_15, turtle_16, turtle_17, turtle_18, turtle_19, turtle_20]
    turtle_status[turtle_1] = "Awake"
    turtle_status[turtle_2] = "Awake"
    turtle_status[turtle_3] = "Awake"
    turtle_status[turtle_4] = "Awake"
    turtle_status[turtle_5] = "Awake"
    turtle_status[turtle_6] = "Awake"
    turtle_status[turtle_7] = "Awake"
    turtle_status[turtle_8] = "Awake"
    turtle_status[turtle_9] = "Awake"
    turtle_status[turtle_10] = "Awake"
    turtle_status[turtle_11] = "Awake"
    turtle_status[turtle_12] = "Awake"
    turtle_status[turtle_13] = "Awake"
    turtle_status[turtle_14] = "Awake"
    turtle_status[turtle_15] = "Awake"
    turtle_status[turtle_16] = "Awake"
    turtle_status[turtle_17] = "Awake"
    turtle_status[turtle_18] = "Awake"
    turtle_status[turtle_19] = "Awake"
    turtle_status[turtle_20] = "Awake"

wn = turtle.Screen()
wn.title("Pablo & Emily")
wn.bgcolor("#E5E4E2")
wn.screensize(800,800)
wn.colormode(255) 

while(1==1):
    for item in turtles:        
        item.shape("turtle")  
        current_color = turtle_colors[item]
        item.color(current_color)
        
        if(turtle_status[item]=="Exercising"):  
            item.speed(20)
            item.pendown()
            item.forward(random.randrange(30, 120))
            item.right(90)
            item.right(random.randrange(-180, 180))

        if(turtle_status[item]=="Awake"):
            item.penup()
            item.speed(100)
            item.goto(turtle_position_x[item],turtle_position_y[item])
            item.left(random.randrange(-180, 180))
            turtle_status[item] = "Exercising"
        
wn.mainloop()  

print("----------------------------------------");