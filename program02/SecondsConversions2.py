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
print("Program 02B Seconds Conversions");
print("A&B");
print("************************************");

import math

seconds = 0
days = 0
hours = 0
minutes= 0

output_hours   = "Hours"
output_minutes = "Minutes"
output_seconds = "Seconds"

seconds_input = int(input("Please enter a number of seconds: "));
seconds = seconds_input

hours = (seconds/3600)
hours = math.floor(hours) 
seconds = (seconds - (hours*3600))

minutes = (seconds/60)
minutes = math.floor(minutes) 
seconds = (seconds - (minutes*60))

if(hours == 1):
    output_hours = "Hour"
else:
    output_hours = "Hours"

if(minutes == 1):
    output_minutes = "Minute"
else:
    output_minutes = "Minutes"

if(seconds == 1):
    output_seconds = "Second"
else:
    output_seconds = "Seconds"

print("Seconds entered: "+ str(seconds_input) + "");
print("\nResults:")
print("----------------------------------------")
print(""+ str(output_hours) +":    "+ str(hours) + "");
print(""+ str(output_minutes) +": "+ str(minutes) + "");
print(""+ str(output_seconds) +": "+ str(seconds) + "");

#Above and beyond
import time
hr = int(time.strftime("%H"))
mn = int(time.strftime("%M"))
sc = int(time.strftime("%S"))

if(hr == 1):
    output_hr = "Hour"
else:
    output_hr = "Hours"

if(mn == 1):
    output_mn = "Minute"
else:
    output_mn = "Minutes"

if(sc == 1):
    output_sc = "Second"
else:
    output_sc = "Seconds"

"""For our above and beyond we took this idea and instead of having user input,
we had the program draw time information from the computer. Because we can get this 
information already divided into hours/minutes/seconds, it was relatively easy for
it to output these values for distance from midnight, and we just applied the same
conditional statements to ensure proper grammar."""


print("----------------------------------------")
t = str(input("do you want to know how long it has been since midnight? (y/n) "))
if t == "y" or t == "Y" or t == "n" or t == "N":
    print("Input recognized.")
    if t == "y" or t == "Y":
        print("You would like to know!")
        print(""+ str(output_hr) +":    "+ str(hr) + "");
        print(""+ str(output_mn) +": "+ str(mn) + "");
        print(""+ str(output_sc) +": "+ str(sc) + "");  
    else:
        print("You don't want to know. fine.")
else:
    print("Input not recognized.")
print("----------------------------------------")