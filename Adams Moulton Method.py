#Adams Moulton Method:
#implicit corrector Method

import numpy as np 

ynp1 = 0.6841
yn  = 0.4228
ynm1 =  0.2027
ynm2 = 0

xnp1 = 0.6
xn  = 0.4
xnm1 =  0.2
xnm2 = 0

n = 2

h = 0.2
order = 4

def dy(x,y):
    dyvalue = 1 + y**2
    return dyvalue


i = 0
if order == 2:
    print("order2")
    while i<=n:
        ynp1 = yn + h*(dy(xnp1,ynp1)+dy(xn,yn))*0.5
        print("____________"+str(i)+"____________")
        print("ynp1 = "+ str(ynp1))
        print("xnp1 = "+ str(xnp1))
        xnp1+=h
        yn = ynp1
        xn+=h
        i+=1
elif order == 3:
    print("order3")
    while i<=n:
        ynp1 = yn + h*(5*dy(xnp1,ynp1)+8*dy(xn,yn)-dy(xnm1,ynm1))/12
        print("____________"+str(i)+"____________")
        print("ynp1 = "+ str(ynp1))
        print("xnp1 = "+ str(xnp1))
        xnp1+=h
        xnm1+=h
        xnp1+=h
        ynm1 = yn
        yn = ynp1
        xn+=h
        i+=1
elif order ==4:
    print("order4")
    while i<=n:
        ynp1 = yn + h*(9*dy(xnp1,ynp1)+19*dy(xn,yn)-5*dy(xnm1,ynm1)+dy(xnm2,ynm2))/24
        print("____________"+str(i)+"____________")
        print("ynp1 = "+ str(ynp1))
        print("xnp1 = "+ str(xnp1))
        xnp1+=h
        ynm2 = ynm1
        xnm2+=h
        xnm1+=h
        ynm1 = yn
        yn = ynp1
        xn+=h
        i+=1