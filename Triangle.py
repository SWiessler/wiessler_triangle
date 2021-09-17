# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'NotATriangle'

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'NotATriangle'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'NotATriangle'
    
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == c:
        return 'Equilateral'
    elif (((a ** 2) + (b ** 2)) == (c ** 2)) or (((b ** 2) + (c ** 2)) == (a ** 2)) or (((a ** 2) + (c ** 2)) == (b ** 2)):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isoceles'

#if __name__ == '__main__':
    # running classify triangle through main
    # right triangle
    #print(classifyTriangle(5, 12, 13))
    # equilateral
    # print(classifyTriangle(5, 5, 5))
    # isoceles
    # print(classifyTriangle(11,11,20))
    # # scalene
    # #print(classifyTriangle(10,15,20))
    # # invalid - 'NotATriangle'
    # print(classifyTriangle("zoinks",4,5))
    # print(classifyTriangle(-1,4,4))
    # print(classifyTriangle(0,4,4))
    # print(classifyTriangle([20],4,4))