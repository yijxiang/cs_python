# -*- coding: utf-8 -*-
"""
***********************************************
Pablo Fernandez 
Quinn Salkind
Copyright 2016, www.pablofernandez.com
***********************************************
"""

"""
Above and Beyond, the user is given the option for the
program to produce multiple polygons according to the 
specifications of the user, including distance, and radius. 

"""

print("************************************")
print("Pablo Fernandez")
print("Quinn Salkind")
print("Program 02A Godzilla Loves Polygons")
print("A&B: Multiple User Options Included")
print("************************************")

import turtle 
import math    

mysides = 0
myradius = 0   
multiple = ""

def RegularPolygon(t,n,r):
    """Given a turtle, t, and a number of sides, n, and a radius to the vertex, r, 
    will draw a regular n sided polygon. This is centered around the starting point"""
    t.penup()
    t.forward(r)
    t.left((180/n)+(90-(360/n)))
    t.pendown()
    for i in range(n):
        t.left(360/n)  
        t.forward(2*math.sin(((180/n)*math.pi)/180)*r)    
    t.penup()
    t.right(90 - (180/n))
    t.backward(r)
    
mysides  = int(input("How many sides would you like: "))
myradius = int(input("What would you like for the radius: "))
multiple = str(input("Would you like multiple polygons (yes/no): "))
if((multiple == "yes") | (multiple == "YES")):
    apart    = int(input("How far apart would you like the turtles: "))
else:
    print("Next time you should try multiple polygons!")

wn = turtle.Screen()
wn.title("Pablo & Quinn")
wn.bgcolor("#0069b2")
wn.colormode(255) 

godzilla = turtle.Turtle()
godzilla.color("#f47b09")
godzilla.shape("turtle")
godzilla.speed(5)
godzilla.stamp()
RegularPolygon(godzilla,mysides,myradius)


if((multiple == "yes") | (multiple == "YES")):
    godzilla.forward(apart+myradius)
    godzilla.stamp()
    RegularPolygon(godzilla,mysides,myradius)
    godzilla.right(90)
    godzilla.forward(apart+myradius)
    godzilla.stamp()
    RegularPolygon(godzilla,mysides,myradius)
    godzilla.right(90)
    godzilla.forward(apart+myradius)
    godzilla.stamp()
    RegularPolygon(godzilla,mysides,myradius)
    godzilla.forward(apart+myradius)
    godzilla.stamp()
    RegularPolygon(godzilla,mysides,myradius)
    godzilla.right(90)
    godzilla.forward(apart+myradius)
    godzilla.stamp()
    RegularPolygon(godzilla,mysides,myradius)  
    godzilla.forward(apart+myradius)
    godzilla.stamp()
    RegularPolygon(godzilla,mysides,myradius)  
    godzilla.right(90)
    godzilla.forward(apart+myradius)
    godzilla.stamp()
    RegularPolygon(godzilla,mysides,myradius)   
    godzilla.forward(apart+myradius)
    godzilla.stamp()
    RegularPolygon(godzilla,mysides,myradius) 
    
wn.mainloop()  
