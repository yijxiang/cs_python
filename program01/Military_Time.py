# -*- coding: utf-8 -*-
"""
Pablo Fernandez 
Copyright 2016, www.PabloFernandez.com
"""

print("************************************");
print("Pablo Fernandez");
print("Lab Partner");
print("Program 01");
print("************************************");

import math

hour = 0
alarm = 0
military_current = 0
military_final = 0
days_final=0

slot = ""
addon = ""

hour = int(input("Please enter the current time (1-12): "));
slot = str(input("Please enter AM/PM: "));
alarm = int(input("In how many hours should the alarm go off: "));

""" Convert inpput to Military Time """
if((slot=="AM") | (slot=="am")):
    military_current = hour
if((slot=="PM") | (slot=="pm")):
    military_current = (hour + 12)

military_final = military_current + alarm

if(alarm>=24):
    days_final = math.floor((alarm / 24))
    military_final = (military_final - (days_final*24))
    addon = "am"
elif(alarm>12):
    military_final = (military_final - 12)
    addon = "pm"
else:
    addon =""

if(addon==""):
    if(military_final>12):
        military_final = military_final -12
        addon = "pm"
    elif(military_final<12):
        addon = "am"
    else:
        addon = "am"

print("\nResults:")
print("----------------------------------------")
print("Alarm set for: "+ str(military_final) + "" + str(addon) + "");
print("Days: "+ str(days_final) + "");

