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

Term_Back_2 = 1;
Term_Back = 2;
Current = 0;

Even_Sum = 0;
Even_Sum = Even_Sum + Term_Back;

while(Current<4000000):    
    Current = (Term_Back_2 + Term_Back)
    if(Current % 2 == 0):
        Even_Sum = (Even_Sum + Current)
    Term_Back_2 = Term_Back
    Term_Back = Current
        
print("Sum of all even fibonacci sequence numbers under 4 million");
print("Computed Answer: "+str(Even_Sum)+"")    

print("----------------------------------------");