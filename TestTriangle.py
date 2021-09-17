# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(4,4,4),'Equilateral','4,4,4 is an Equilateral triangle')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(10,15,20),'Scalene','10,15,20 is a Scalene triangle')
    
    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(11,11,20),'Isoceles','11,11,30 is an Isoceles triangle')

    # invalid input
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle("zoinks",4,5),'NotATriangle','zoinks,4,5 is NotATriangle')
    
    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(-1,4,4),'NotATriangle','-1,4,4 is NotATriangle')
    
    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(0,4,4),'NotATriangle','0,4,4 is NotATriangle')
    
    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle([20],4,4),'NotATriangle','[20],4,4 is NotATriangle')

    def testInvalidInputE(self):
        self.assertEqual(classifyTriangle(10.5,10.5,20),'NotATriangle','10.5,10.5,30 is NotATriangle')
    
    # sides do not equal a triangle
    def testNonviableSideA(self):
        self.assertEqual(classifyTriangle(3,4,8),'NotATriangle','3,4,8 is NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

