# -*- coding: utf-8 -*-
"""
***********************************************
Pablo Fernandez 
Quinn Salkind
Copyright 2016, www.pablofernandez.com
***********************************************
"""

print("************************************");
print("Pablo Fernandez");
print("Quinn Salkind");
print("Program 02A Godzilla Loves Polygons");
print("************************************");

import turtle 
import math    

mysides = 0
myradius = 0   

def RegularPolygon(godzilla,n,r):
    """Given godzilla, and a number of sides, n, and a radius to the vertex, r, 
    will draw a regular n sided polygon. This is centered around 0"""
    godzilla.penup()
    godzilla.forward(r)
    godzilla.left((180/n)+(90-(360/n)))
    godzilla.pendown()
    for i in range(n):
        godzilla.left(360/n)  
        godzilla.forward(2*math.sin(((180/n)*math.pi)/180)*r)    
    godzilla.penup()
    godzilla.setpos(0,0)
    godzilla.setheading(0)
    godzilla.forward(r)
    godzilla.pendown()
    godzilla.left(90)
    godzilla.circle(r,None,None)
    godzilla.penup()
    godzilla.setpos(0,0)
    
mysides = int(input("How many sides would you like: "));
myradius = int(input("What would you like for the radius: "));

wn = turtle.Screen()
wn.title("Pablo & Quinn")
wn.bgcolor("#0069b2")
wn.colormode(255) 

godzilla = turtle.Turtle()
godzilla.color("#f47b09")
godzilla.shape("turtle")
godzilla.speed(5)

RegularPolygon(godzilla,mysides,myradius)

wn.mainloop()   

