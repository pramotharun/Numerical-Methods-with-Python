# Taylor Series Method

import numpy as np 
import sympy as sp 
from scipy.misc import derivative
x = 0

n = 4 # how many values of y should be found? #####Input!
y0 = 1
h = 0.1




def dy(x,y):
    answer1 = 2*x+3*y # Enter the y' here!!!1  change this!
    return answer1

def ddy(x,y,first_derivative):
    answer2 = 2+3*(2*x+3*y) # Enter the y'' here!!!1  change this!
    return answer2

def dddy(x,y,first_derivative, second_derivative):
    answer3 = 2+2*y+2*((x**2)*(1+y))*x+(2*x+2*x*y+((x**2)*(1+y))*(x*x))*(x*x)+2*x*((x**2)*(1+y)) # Enter the y''' here!!!1  change this! Only is order is 3 and uncoment the eq below
    return answer3

def ddddy(x,y,first_derivative, second_derivative, third_derivative):
    answer3 = 2 + 6*x + 9*y # Enter the y''' here!!!1  change this! Only is order is 3 and uncoment the eq below
    return answer3

y = y0


i =1
while i<=n:
    first_derivative = dy(x,y)
    second_derivative = ddy(x,y,first_derivative)
    third_derivative = dddy(x,y,first_derivative,second_derivative)
    fourth_derivative = ddddy(x,y,first_derivative,second_derivative,third_derivative)
    ynew = y + h*(first_derivative) + (h**2)*(second_derivative)*0.5 #+ (h**3)*(third_derivative)/6 #+ (h**4)*(fourth_derivative)/24
    print("y number =")
    print(i)
    print("\n")
    print("y = ")
    print(ynew)
    print("\n")
    i+=1
    y = ynew
    x+=h

print(ynew)
