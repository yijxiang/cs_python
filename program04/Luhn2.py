# -*- coding: utf-8 -*-
"""
***********************************************
Pablo Fernandez 
Eloise Coutret
Copyright 2016, www.pablofernandez.com
***********************************************
"""

print("************************************");
print("Pablo Fernandez");
print("Eloise Coutret");
print("Program 04 Luhn Algorithm");
print("A&B:");
print("************************************");

"""

"""

def check_luhn(card, valid):
    card_number =[]
    
    iteration = 0
    iteration_next = 0
    value = 0
    
    sum = ""
    
    for iteration in range(16):
        iteration_next = iteration + 1
        value = card[iteration:iteration_next]
        card_number.insert(iteration, value)
        iteration = iteration + 1
        
    term_1  = card_number[0]
    term_2  = card_number[1]
    term_3  = card_number[2]
    term_4  = card_number[3]
    term_5  = card_number[4]
    term_6  = card_number[5]
    term_7  = card_number[6]
    term_8  = card_number[7]
    term_9  = card_number[8]
    term_10 = card_number[9]
    term_11 = card_number[10]
    term_12 = card_number[11]
    term_13 = card_number[12]
    term_14 = card_number[13]
    term_15 = card_number[14]
    term_16 = card_number[15]

    term_15_a = 0
    term_15_b = 0
    term_15 = (term_15 * 2)
    term_15_a = term_15[0:1]
    term_15_b = term_15[1:2]
    
    term_13_a = 0
    term_13_b = 0
    term_13 = (term_13 * 2)
    term_13_a = term_13[0:1]
    term_13_b = term_13[1:2]

    term_11_a = 0
    term_11_b = 0
    term_11 = (term_11 * 2)
    term_11_a = term_11[0:1]
    term_11_b = term_11[1:2]

    term_9_a = 0
    term_9_b = 0
    term_9 = (term_9 * 2)
    term_9_a = term_9[0:1]
    term_9_b = term_9[1:2]

    term_7_a = 0
    term_7_b = 0
    term_7 = (term_7 * 2)
    term_7_a= term_7[0:1]
    term_7_b = term_7[1:2]

    term_5_a = 0
    term_5_b = 0
    term_5 = (term_5 * 2)
    term_5_a = term_5[0:1]
    term_5_b = term_5[1:2]

    term_3_a = 0
    term_3_b = 0
    term_3 = (term_3 * 2)
    term_3_a = term_3[0:1]
    term_3_b = term_3[1:2]

    term_1_a = 0
    term_1_b = 0
    term_1 = (term_1 * 2)
    term_1_a = term_1[0:1]
    term_1_b = term_1[1:2]

    sum = (int(term_1_a) + int(term_1_b) + int(term_2) + int(term_3_a) + int(term_3_b) + int(term_4))
    sum = sum + (int(term_5_a) + int(term_5_b) + int(term_6) + int(term_7_a) + int(term_7_b) + int(term_8))
    sum = sum + (int(term_9_a) + int(term_9_b) + int(term_10) + int(term_11_a) + int(term_11_b) + int(term_12))
    sum = sum + (int(term_13_a) + int(term_13_b) + int(term_14) + int(term_15_a) + int(term_15_b) + int(term_16))
    
    print("SUM: "+str(sum)+". ")    


    amex = card[0:2]
    disc_1 = card[0:4]
    disc_2 = card[0:3]
    disc_3 = card[0:2]
    mast = card[0:2]    
    visa = card[0:1]    

    if(amex == "34"):
        type = "AmEx"
    elif(amex == "37"):
        type = "AmEx"
    elif((disc_1=="6011") | (disc_2=="6011") | (disc_3=="6011")):
        type = "Discover"
    elif((disc_1=="644") | (disc_2=="644") | (disc_3=="644")): 
        type = "Discover"
    elif((disc_1=="65") | (disc_2=="65") | (disc_3=="65")):   
        type = "Discover"
    elif(mast=="51"): 
        type = "Mastercard"
    elif(mast=="52"): 
        type = "Mastercard"
    elif(mast=="53"): 
        type = "Mastercard"
    elif(mast=="54"): 
        type = "Mastercard"
    elif(mast=="55"): 
        type = "Mastercard"
    elif(visa == "4"):
        type = "Visa"
    else:
        type= "Unkown"
    
    print("Card type: "+str(type)+"")    
    
    valid = sum 
    return valid    
    
    
card = ""
valid = 0

card = str(input("Please enter a credit card number in the format: (XXXX XXXX XXXX XXXX): "));
card = card.replace(" ", "")

valid = check_luhn(card, valid)


if(valid == 1):
    print ("Your card is valid")
else:
    print ("Your card is invalid")

print("----------------------------------------");