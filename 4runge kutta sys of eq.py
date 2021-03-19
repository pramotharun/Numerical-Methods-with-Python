#Runge kutta system of equations
import numpy as np 

def dy(x,y,z):
    dyvalue = z
    return dyvalue
 #Note: change the derivative function based on question!!!!!!  Example: y-x


def dz(x,y,z):
    dyvalue = x*(z**2)-y**2
    return dyvalue
 #Note: change the derivative function based on question!!!!!!  Example: y-x

z = 0
y0 = 3 # input y for xo
x = 0
h = 0.2
y = y0
finalx = 0.4
interval = finalx - x
n = interval/h
i = 1



while i<=n:
    print("_________________" + str(i)+ "_________________"+"\n")
    k1 = dy(x,y,z) *h
    print("k1= "+str(k1))
    l1 = dz(x,y,z) *h
    print("l1= "+str(l1))
    k2 = dy(x+h*0.5,y+k1*0.5,z+l1*0.5) *h
    print("k2= "+str(k2))
    l2 = dz(x+h*0.5,y+k1*0.5, z+l1*0.5) *h
    print("l2= "+str(l2))
    k3 = dy(x+h*0.5,y+k2*0.5, z+l2*0.5) *h
    l3 = dz(x+h*0.5,y+k2*0.5, z+l2*0.5) *h
    print("l3= "+str(l3))
    print("k3= "+str(k3))
    k4 = dy(x+h,y+k3, z+l3) *h
    print("k4= "+str(k4))
    l4 = dz(x+h,y+k3, z+l3) *h
    print("l4= "+str(l4))
    y = y + (k1+2*k2+2*k3+k4)/6
    z = z + (l1+2*l2+2*l3+l4)/6
    x = x+h
    i+=1
    print("\n")
    print("y =       " + str(y))
    print("\n")
    print("z =       " + str(z))
    print("\n")
