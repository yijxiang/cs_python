# -*- coding: utf-8 -*-
"""
***********************************************
Pablo Fernandez 
Copyright 2016, www.pablofernandez.com
***********************************************
"""

print("************************************");
print("Pablo Fernandez");
print("Partner: Salkind, Quinn");
print("Program 01 Turtles");
print("************************************");

import turtle
import math

count = 0
rotate = 0
mysides = 0
myradius = 0


def RegularPolygon(myturtle,mysides,myradius):
    pabs.stamp()
    rotate = 360/mysides;
    outside_length = (math.sin(rotate/2)*(myradius/math.sin(rotate/2)))
    pabs.forward(outside_length)
    pabs.right(rotate)
    for count in range(mysides):        
        pabs.forward(outside_length/2)
        pabs.right(rotate)
        pabs.forward(outside_length/2)

mysides = int(input("How many sides would you like: "));
myradius = int(input("What would you like for the radius: "));

wn = turtle.Screen()     
wn.bgcolor("#0069b2")
wn.colormode(255)    
wn.title("Pablo & Quinn")

pabs = turtle.Turtle()       
pabs.color("#f47b09")
pabs.shape("turtle")
pabs.speed(0)

RegularPolygon(pabs,mysides,myradius)




"""
        print(""+ str(outside_length) +"")                

        pabs.penup()
        pabs.forward(myradius)
        pabs.pendown()
        pabs.right(rotate/2)  
        pabs.forward(myradius)

    pabs.setposition(0,0)
"""
"""
def RegularPolygon(t,n,s):
    for i in range(n):        # says do what follows 5 times
        t.forward(s)          # indenting groups statements together
        t.left(360/n)    
        

# call the function
for i in range(50):
    alex.penup()
    alex.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))    
    alex.setpos(random.randint(-150,150),random.randint(-150,150))
    alex.pendown()
    alex.right(random.randint(1,360))
    RegularPolygon(alex,random.randint(3,10),random.randint(10,30))
    
wn.mainloop()             # Wait for user to close window

"""








wn.mainloop()