# -*- coding: utf-8 -*-
#Pablo Fernandez and Jenna Stanley
"""
Created on Tue Feb  2 21:03:23 2016

@author: jennastanley
"""


def find_number_3_multiples(x):
    """Calculate the number of times that 3 goes into x."""
    mult3=x//3
    return mult3


def sum_3_multiples(y):
    """Calculate the sum of the multiples of 3."""
    sum3=0
    for i in range(1, y+1):
        num_to_add=3*i
        sum3=sum3+num_to_add
    return sum3


def find_number_5_multiples(z):
    """Calculate the number of times 5 goes into z."""
    mult5=z//5
    return mult5
    

def sum_5_multiples(t):
    """Calculate the sum of the multiples of 5"""
    sum5=0
    for i in range(1, t+1):
        num_to_add=5*i
        if (num_to_add)%3==0:       #avoid adding numbers that are multiples of 3 and 5 twice
            continue
        sum5=sum5+num_to_add
    return sum5


def sum_of_3_and_5_multiples(s3,s5):
    """Calculate the sum of the multiples of 3 and 5."""
    totalsum=s3+s5
    return totalsum


def report_total_sum(summ):
    print("The sum of all the multiples of 3 or 5 below 1000 is " +str(summ))


a=find_number_3_multiples(999) #avoid counting 1000 as one of the multiples of 5.(user input minus 1)
b=sum_3_multiples(a)
c=find_number_5_multiples(999) #(user input minus 1)
d=sum_5_multiples(c)
e=sum_of_3_and_5_multiples(b,d)
report_total_sum(e)
