# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:55:03 2016

@author: jennastanley
"""

# -*- coding: utf-8 -*-
"""
***********************************************
Pablo Fernandez 
Jenna Stanley
Copyright 2016, www.pablofernandez.com
***********************************************
"""
import random
print("************************************");
print("Pablo Fernandez");
print("Jenna Stanley");
print("Program 03A Even Fibonacci");
print("A&B:");
print("************************************");
def user_hailstone():
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
    
    start = int(input("Please enter a positive starting integer: "));
    print("You entered "+str(start)+".")
    while(start<=0):     #because otherwise it never stops
        print("Invalid Input!");
        start = int(input("Please enter a positive starting integer: "));
    
    Hailstone.insert(0, start)
    current_term = start
    
    print(""+str(iteration_num)+". Value: "+str(current_term)+"")
    
    while(Hailstone[iteration_num]!=1):
            
        if(Hailstone[iteration_num]%2==0):
            current_term = (Hailstone[iteration_num] / 2) 
            iteration_num = iteration_num + 1
            Hailstone.insert(iteration_num, current_term)
        else:
            current_term = ((3*Hailstone[iteration_num])+1)
            iteration_num = iteration_num + 1
            Hailstone.insert(iteration_num, current_term)
            
        print(""+str(iteration_num)+". Value: "+str(int(current_term))+"")  #without decimal points?
    
    return(int(iteration_num))
    

def random_hailstone():
    Hailstone=[]
    start = 0
    current_term = 0
    iteration_num = 0 
    
    start = int(random.randint(2,150));
    
    Hailstone.insert(0, start)
    current_term = start
    
    print(""+str(iteration_num)+". Value: "+str(current_term)+"")
    
    while(Hailstone[iteration_num]!=1):
            
        if(Hailstone[iteration_num]%2==0):
            current_term = (Hailstone[iteration_num] / 2) 
            iteration_num = iteration_num + 1
            Hailstone.insert(iteration_num, current_term)
        else:
            current_term = ((3*Hailstone[iteration_num])+1)
            iteration_num = iteration_num + 1
            Hailstone.insert(iteration_num, current_term)
            
        print(""+str(iteration_num)+". Value: "+str(int(current_term))+"")  #without decimal points?
    
    return(int(iteration_num))


#Now back to the user interface.
x=user_hailstone()
user=int(input("Do you want to know the number of iterations of your requested sequence? If yes, enter 1. If no, enter 2. "))
if user==1:
    print("It took "+str(x)+" iterations to reach 1.")
elif user==2:
    giraffe=int(input("Would you like to use the Hailstone sequence using a random integer? Enter 1 for yes or 2 for no: "))
    if giraffe==1:
        y=random_hailstone()
        print("It took "+str(y)+" iterations to reach 1 using the randomly generated integer.")
    else:
        print("End of program.")
else:
    print("End of program.")


print("----------------------------------------");