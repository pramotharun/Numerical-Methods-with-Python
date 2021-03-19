#Eulers method
import numpy as np

def dy(ynew,xnew,y,x,h):
    dyvalue = y-x
    return dyvalue
 #Note: change the derivative function based on question!!!!!!  Example: y-x

y0 = 0.5  #float(input"what is the y(0)?")

h = 0.1 #float(input"h?")

x_final = 0.3 #float(input"x_final")

#initiating input variables
x = 0
y = y0
# remember to change yn+1 and xn+1 values if you already know them!!!
ynew = 0
xnew = 0
i = 0

#####################################################
iterations = x_final/h

while x <= x_final:
    derivative_of_y = dy(ynew,xnew,y,x,h)
    xnew = x + h 
    ynew = y + (xnew - x)*(derivative_of_y)
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

