# -*- coding: utf-8 -*-
"""
***********************************************
Pablo Fernandez 
Copyright 2016, www.pablofernandez.com
***********************************************
"""

print("************************************");
print("Pablo Fernandez");
print("Program 06 Sort and Search");
print("A&B: Dragon game featuring random outcomes");
print("************************************");

import random
import time
 
imported_numbers = []

new_file = "sorted.dat"
file_name = ""
above = ""
user_input_str = "9999"
user_input = 0.0
location = 0.0
    
def importing_data(file_name, imported_numbers):  
    print("Data Imported")
    print("-------------------------")
    with open(file_name, "r") as ins:
        for line in ins:
            line = line.rstrip()
            line = float(line)
            imported_numbers.append(line)
    ins.close()
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
            if(user_input == temporary):
                i = i + 1
            size_of = len(imported_numbers)
            location = int((i / size_of) * 100)
            break
        
    if(user_input > largest_entry):
        location = 100
        
    if(user_input < smallest_entry):
        location = 0
        
    return location

def export_file(imported_numbers, new_file):
    file = open(new_file,'w') 
    for line in imported_numbers:
        line = str(line)
        file.write(line)
        file.write("\n")
    file.close()
    print("Success: Data has been written to " + new_file)
    
    
"""
Above and Beyond
Mini Dragon Game
Based on the path you choose in a Dragon world where you may survive
and live another day, or be gobbled up whole. You might even find
treasure. 
"""

def above_beyond():
    
    print('')
    print('You are in a mysterious land full of dragons. ')
    print('As you are traveling along an abandoned trail,')
    print('you stumble upon a cave and an abandoned mine.')
    print('1. Enter the dark cave')
    print('2. Enter the spooky mine')
    choice_a = ''
    choice_b = ''

    first_obstacle = ''
    second_obstacle = ''
    
    chance_1 = random.randrange(2) 
    chance_2 = random.randrange(3) 

    while (choice_a != '1' and choice_a != '2'):
        choice_a = str(input('Option: '))
    if(choice_a=="1"):
        first_obstacle = "cave"
    if(choice_a=="2"):       
        first_obstacle = "mine"
    print("")

    print('You approach the '+ first_obstacle + '...')
    time.sleep(1)
    if(chance_2==3):
        print('It is very dark and cold inside...')
    else:
        print('It is very hot and slimy inside...')
    time.sleep(2)
    print('You continue walking through as quietly as possible...')
    print()
    time.sleep(2)
    
    print('Suddenly you hear something move to your left!')
    print('1. Begin running from the noise!')
    print('2. Stay and defend your territory!') 
        
    while (choice_b != '1' and choice_b != '2'):
        choice_b = str(input('Option: '))
    if(choice_b=="1"):
        second_obstacle = "run away from any danger!"
    if(choice_b=="2"):       
        second_obstacle = "stay and fight!"
    print("")

    print('You decide to '+ second_obstacle + '...')
    time.sleep(2)
    
    if(choice_b=="1"):
        print('A dragon suddenly appears from within the ' + first_obstacle + '...')
        time.sleep(2)
        if(chance_1==1):
            print("And eats you up in one bite...")
            print("Game over.")
        else:
            print("You continue running as fast as possible...")
            time.sleep(2)
            if(chance_2==1):
                print("You aren't as fast as he is. He gobbles you down in one bite...")
                print("Game over.")
            else:
                print("You manage to lose him in the dark! Congratulations you survived!")
                print("Game over.")

    if(choice_b=="2"):
        print('A dragon suddenly appears from within the ' + first_obstacle + '...')
        time.sleep(1)
        if(chance_2==1):
            print("And decides to give you his treasure! Congratulations you survived!")
            print("Game over.")
        else:
            print("Being a brave knight, you decide to fight the monster...")
            time.sleep(2)
            if(chance_1==1):
                print("You are no match for his strength. He gobbles you down in one bite...")
                print("Game over.")
            else:
                print("He is not very hungry, and decides to fly away! Congratulations you survived!")
                print("Game over.")
    print("----------------------------------------");
       
above = str(input("Would you like to run the Above and Beyond (Y/N): "));
if((above=="Y") | (above=="y")):
    above_beyond()

print("")
file_name = str(input("Please enter the name of a file to read: "));
imported_numbers = importing_data(file_name, imported_numbers)

while(1==1):
    user_input_str = str(input("Please enter a floating point number:  "));  
    if(user_input_str==""):
        break
    else:
        user_input = float(user_input_str)
        location = calculate_location(imported_numbers, user_input, location)
        print("The rank is: " + str(location) + "%")
        check_exist = str(user_input)
        export_file(imported_numbers, new_file)
        
print("Thank you for using the program!");
print("----------------------------------------");