# -*- coding: utf-8 -*-
"""
***********************************************
Pablo Fernandez 
Quinn Salkind
Copyright 2016, www.pablofernandez.com
***********************************************
"""

"""
Above & Beyond

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