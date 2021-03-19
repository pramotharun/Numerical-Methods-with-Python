#Modified Euler / Heuns method:
#Runge Kutta Second (2) Order Method
import numpy as np 


def dy(ynew,xnew,y,x,h):
    dyvalue = x**2 + y**2
    return dyvalue
 #Note: change the derivative function based on question!!!!!!  Example: y-x

y0 = 2.3  #float(input"what is the y(0)?")

h = 0.1  #float(input"h?")

x_final = 1.2 #float(input"x_final")

#initiating input variables
x = 1
y = y0
# remember to change yn+1 and xn+1 values if you already know them!!!
ynew = 0
xnew = 0
i = 0

#####################################################
iterations = x_final/h

while x <= x_final:
    k1 = dy(ynew,xnew,y,x,h)
    k2 = dy(ynew,xnew,y+k1*h,x+h,h)
    xnew = x + h 
    ynew = y + (h/2)*(k1+k2)
    print("iteration:        ____            ")
    print(i)
    print("\n")
    print("x = ")
    print(xnew)
    print("\n")
    print("y = ")
    print(ynew)
    x = xnew
    y = ynew
    i+=1

