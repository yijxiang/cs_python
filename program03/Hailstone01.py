# -*- coding: utf-8 -*-
"""
***********************************************
Pablo Fernandez 
Jenna Stanley
Copyright 2016, www.pablofernandez.com
***********************************************
"""

print("************************************");
print("Pablo Fernandez");
print("Jenna Stanley");
print("Program 03A Even Fibonacci");
print("A&B:");
print("************************************");

Hailstone=[]
start = 0
current_term = 0
iteration_num = 0 

"""
Request a starting integer n0 from the user. Keep requesting the integer until it is positive.
Use a while loop to compute the length of the requested sequence.
Provide user feedback.
Offer to show the terms of the sequence upon request.
Report the length of the requested sequence.
Have a well-designed input and reporting scheme.
An Above & Beyond comment.
"""

start = int(input("Please enter a starting integer: "));
while(start<0):
    print("Invalid Input!");
    start = int(input("Please enter a starting integer: "));

Hailstone.insert(0, start)
current_term = start

print(""+str(iteration_num)+". Value: "+str(current_term)+"")
while(Hailstone[iteration_num]!=1):
    if(Hailstone[iteration_num]==1):
        current_term = 1
        
    elif(Hailstone[iteration_num]%2==0):
        current_term = (Hailstone[iteration_num] / 2) 
        iteration_num = iteration_num + 1
        Hailstone.insert(iteration_num, current_term)
    else:
        current_term = ((3*Hailstone[iteration_num])+1)
        iteration_num = iteration_num + 1
        Hailstone.insert(iteration_num, current_term)
                
    print(""+str(iteration_num)+". Value: "+str(current_term)+"")

print("----------------------------------------");