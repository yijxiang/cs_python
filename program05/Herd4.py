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
The status of the turtles is constantly tracked including states such
as sleeping, awake, exercising, and tired. These states change depending
on the physical activity that the Turtle has during the day. Normally
the Turtle should finish resting and continue on with its day. 
"""

import turtle 
import random

turtles =[]
turtle_status = {}
turtle_colors = {}
turtle_position_x = {}
turtle_position_y = {}
turtle_distance_traveled = {}

n = 99999
while((n>20) | (n<1)):
    n = int(input("How many turtles would you like (1-20):  "))

for i in range(n):
    temporary_turtle = turtle.Turtle()
    turtles.append(temporary_turtle)
    turtle_distance_traveled[temporary_turtle] = 0
    turtle_status[temporary_turtle] = "Sleeping"
    turtle_colors[temporary_turtle] = "#%03x" % random.randint(0, 0xFFF)
    turtle_position_x[temporary_turtle] = random.randrange(-400, 400)
    turtle_position_y[temporary_turtle] = random.randrange(-400, 400)
    turtle_status[temporary_turtle] = "Awake"
    
wn = turtle.Screen()
wn.title("Pablo & Emily")
wn.bgcolor("#E5E4E2")
wn.setup(800,800) 
wn.colormode(255) 
wn.register_shape("zzz.gif")

while(1==1):
    for item in turtles:        
        distance = turtle_distance_traveled[item]
        current_color = turtle_colors[item]
        item.color(current_color)
        item.shape("turtle")
        
        if(distance > 400):
            lots_of_energy = random.randrange(1, 20)
            if(lots_of_energy == 12):
                turtle_status[item]="Tired"
                
        if(turtle_status[item]=="Tired"):
            item.shape("zzz.gif")
            item.speed(1)
            wakeup = random.randrange(1, 6)
            if(wakeup == 3):
                turtle_status[item]="Exercising"
                turtle_distance_traveled[item] = 0
                distance = 0

        if(turtle_status[item]=="Exercising"):  
            item.shape("turtle")
            item.speed(20)
            item.pendown()
            move_item = random.randrange(20, 60)
            item.forward(move_item)
            distance = distance + move_item
            direction = random.randrange(1, 6)
            if(direction==1):
                item.left(90)
            if(direction==2):
                item.right(90)
            if(direction==3):
                item.right(0)   
            if(direction==4):
                item.right(45)   
            if(direction==5):
                item.left(45)   

        if(turtle_status[item]=="Awake"):
            item.penup()
            item.speed(100)
            item.goto(turtle_position_x[item],turtle_position_y[item])
            item.left(random.randrange(-180, 180))
            turtle_status[item] = "Exercising"
        
        turtle_distance_traveled[item] = distance
        
wn.mainloop()  

print("----------------------------------------");