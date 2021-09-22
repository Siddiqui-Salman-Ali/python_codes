# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 21:32:18 2021

@author: EngrS
"""

def isPrime(x):
    """The function identifies whether the 
    number passed is prime or not 
    the input to the function is an integer
    and the output is boolean 
    True if number is prime else false"""
    for div in range (2,x//2 +1):
        if x == 2:
            print("Prime")
        elif x % div ==0:
            return False
            break
        else:
            div +=1
    return True
                       
#Implementing fizzbuzz with loops:
          
for num in range(1,101):
    if num%3 == 0 and num%5 ==0:
         print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif isPrime(num) == True:
        print ("Prime")
    else:
        print(num)
        
        
    

            
            
        