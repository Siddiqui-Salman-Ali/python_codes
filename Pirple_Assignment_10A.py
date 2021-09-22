# -*- coding: utf-8 -*-
"""
Created on Sun May 23 02:04:39 2021

@author: EngrS
"""

import numpy as np
from scipy import misc

import matplotlib.pyplot as plt

#Using SciPy package

face = misc.face()
plt.imshow(face)
plt.show()

#creting a python list

A = [1.2 , 3.4 , 5.6 , 6.8 , 8.3 , 0.64]

A_numpy = np.array(A)


print("Rounded values are ",A_numpy.shape)


print("Saured root is ", A_numpy**(0.5))

B = [1 , 9 , 2 ,3 ,6 ,4 ]

B_numpy =np.array(B)

print("The multiplication of both the arrays is " ,(A_numpy * B_numpy)) 

#Creating array of 1's of size same as A

A_Ones = np.ones(A_numpy.shape)

print (A_Ones)

#Creating arrays of 0's size same as B

B_Zeros = np.zeros(B_numpy.shape)

print (B_Zeros)




#Circle approxiamtions using np

class Circle:
    
    def __init__(self, diameter = 0):
        self.diameter = diameter
        
    
    def Area(self):

        area = (np.pi / 4)* np.square(self.diameter)
        print ("The area of the circle is ",area )
        
        return area
    
    def Circumference(self):
        
        circumference =  np.pi * self.diameter
        
        print ("The circumference of the circle is ", circumference)
        
        return circumference
    
    def Plot(self):
        circle1 = plt.Circle((0,0),self.diameter , color = 'r')
        
        fig, ax = plt.subplots()
        ax.set_xlim((-10, 10))
        ax.set_ylim((-10, 10))
        ax.add_patch(circle1)
        plt.show()
        
my_circle = Circle(5)

my_circle.Area()

my_circle.Circumference()

my_circle.Plot()





