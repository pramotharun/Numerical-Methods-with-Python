#Runge Kutta Fourth (4) Order Method
import numpy as np 

def dy(x,y):
    dyvalue = x*y + y**2
    return dyvalue
 #Note: change the derivative function based on question!!!!!!  Example: y-x

y0 = 1 # input y for xo
x = 0
h = 0.1
y = y0
finalx = 0.3
interval = finalx - x
n = interval/h
i = 0



while i<=n:
    print("_________________" + str(i)+ "_________________"+"\n")
    k1 = dy(x,y) *h
    print("k1= "+str(k1))
    k2 = dy(x+h*0.5,y+k1*0.5) *h
    print("k2= "+str(k2))
    k3 = dy(x+h*0.5,y+k2*0.5) *h
    print("k3= "+str(k3))
    k4 = dy(x+h,y+k3) *h
    print("k4= "+str(k4))
    y = y + (k1+2*k2+2*k3+k4)/6
    x = x+h
    i+=1
    print("\n")
    print("y =       " + str(y))
    print("\n")
    print("x =   " + str(x))
    print("\n")
