#Milne's Corrector Predictor Method
import numpy as np 

pynp1 = 0 #predictor
yn  = 1.504119
ynm1 =   1.2773913
ynm2 = 1.1168872
ynm3 =1

xnp1 = 0.4
xn  = 0.3
xnm1 =  0.2
xnm2 = 0.1
xnm3 =0

n = 2

h = 0.1
#order = 4 always

def dy(x,y):
    dyvalue = x*y + y**2
    return dyvalue

i = 0
while i<=n:
    #predictor:

    pynp1 = ynm3 + ((4*h)/3)*(2*dy(xnm2,ynm2)-dy(xnm1,ynm1)+2*dy(xn,yn))


    #corrector:

    cynp1 = ynm1 + (h/3)*(dy(xnm1,ynm1)+4*dy(xn,yn)+dy(xnp1,pynp1))

    #print:

    print("____________"+str(i)+"____________")
    print("xn = "+ str(xnp1))
    print("predictor pyn+1 = "+ str(pynp1))
    print("corrector cyn+1 = "+ str(cynp1))
    print("\n")

    #update:
    ynm3 = ynm2
    ynm2 = ynm1
    ynm1 = yn
    yn = cynp1 #not sure about this. for n >1 should we put the corrected value or the predicted for further iterations

    xnp1+=h
    xnm2+=h
    xnm1+=h
    xn+=h

    i+=1
