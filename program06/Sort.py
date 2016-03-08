# -*- coding: utf-8 -*-
"""
***********************************************
Pablo Fernandez 
"Alec Anderson
Copyright 2016, www.pablofernandez.com
***********************************************
"""

print("************************************");
print("Pablo Fernandez");
print("Alec Anderson");
print("Program 06 Sort and Search");
print("A&B:");
print("************************************");

"""
Above and Beyond
"""
 
import random
import sys


imported_numbers = []

new_file = "sorted.dat"
file_name = ""
user_input_str = "9999"
user_input = 0.0
location = 0.0

def importing_data(file_name, imported_numbers):
    imported_numbers = [2.2, 1.1, 3.3, 8.8, 9.9, 4.4, 5.5, 7.7, 6.6]
    imported_numbers.sort()
    print(imported_numbers)
    return imported_numbers

def calculate_location(imported_numbers, user_input, location):
    size = len(imported_numbers)
    largest_entry = imported_numbers[size-1]
    smallest_entry = imported_numbers[0]

    for i in range (size):
        temporary = 0.0
        temporary = imported_numbers[i]
        if(user_input <= temporary):
            i = i + 1
            location = ((i / 10) * 100)
            break
        
    if(user_input > largest_entry):
        location = 100.00
        
    if(user_input < smallest_entry):
        location = 0.00
        
    return location

def export_file(imported_numbers, new_file):
    file = open(new_file,'w')  
    file.close()

file_name = str(input("Please enter the name of a file to read: "));
imported_numbers = importing_data(file_name, imported_numbers)

while(1==1):
    user_input_str = str(input("Please enter a floating point number:  "));  
    if(user_input_str==""):
        break
    else:
        user_input = float(user_input_str)
        location = calculate_location(imported_numbers, user_input, location)
        print(location)
        check_exist = str(user_input)
        export_file(imported_numbers, new_file)
        
print("Thank you for using the program!");
print("----------------------------------------");