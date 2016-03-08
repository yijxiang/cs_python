# -*- coding: utf-8 -*-
"""
***********************************************
Pablo Fernandez 
Copyright 2016, www.pablofernandez.com
***********************************************
"""

print("************************************");
print("Pablo Fernandez");
print("Nick");
print("Program 01 Turtles");
print("************************************");

import turtle

rotate = 0
counter = 0
size_of_clock = 200
set_speed = 0

size_of_clock = int(input("How big would you like the clock (50-200): "));

wn = turtle.Screen()         
wn.bgcolor("#0069b2")
wn.title("Pablo & Nick")

size = 35
pabs = turtle.Turtle()       
pabs.color("#f47b09")
pabs.shape("turtle")

pabs.speed(set_speed)
pabs.stamp()

while(counter!=12):
    rotate = 30
    pabs.right(rotate)  
    pabs.penup()         
    pabs.forward(size_of_clock)
    pabs.pendown()         
    pabs.forward(20)
    pabs.penup()         
    pabs.forward(20)
    pabs.stamp()    
    
    pabs.forward(50)
    pabs.shape("circle")
    pabs.color("#D4A017")
    pabs.stamp()
    pabs.color("#f47b09")
    pabs.shape("turtle")

    pabs.left(180)
    pabs.forward(size_of_clock+90)   
    pabs.right(180)
    rotate = rotate + 15
    counter = counter + 1
    
wn.mainloop()
