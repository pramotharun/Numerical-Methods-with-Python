#Mutlistep method: Adams Bashforth Method
import numpy as np 

def dy(x,y):
    dyvalue = x - y**2
    return dyvalue

x0= 0 ##least x value known
xp1 = 0.1 
xp2 = 0.2
xp3 = 0.3 #highest x value known

xfinal= 0.3
h = 0.1
n = int(((xfinal - x0)/h)) #if they give limits

y0= 0.854 ## highest i of y value known
ym1 =  0.9145
ym2 = 1
ym3 = 0 ## least y value known


order = 2
##########
x = np.zeros((n+order,1))
y = np.zeros((n+order,1))

i =0

if order == 3:
    p = order -1
    y[p]= y0
    y[p-1]= ym1
    y[p-2]= ym2

    x[p]= xp2
    x[p-1]= xp1
    x[p-2]= x0
    while i<=(n+order):
        print("order3\n")
        y[p+1] = y[p] +(h/12)*(23*dy(x[p],y[p])-16*dy(x[p-1],y[p-1])+5*dy(x[p-2],y[p-2]))
        x[p+1] = x[p] + h
        print("y:"+str(i)+str(y[p+1]))

        p+=1
        i+=1
elif order == 2:
    p = order -1
    y[1]= y0
    y[0]= ym1

    x[1]= xp1
    x[0]= x0
    while i<=(n+order):
        print("order2\n")
        y[p+1] = y[p] +(h/2)*(3*dy(x[p],y[p])-dy(x[p-1],y[p-1]))
        x[p+1] = x[p] + h
        print("y:"+str(i)+str(y[p+1]))

        p+=1
        i+=1
elif order == 4:
    p = order-1
    y[3]= y0
    y[2]= ym1
    y[1]= ym2
    y[0]= ym3

    x[3]= xp3
    x[2]= xp2
    x[1]= xp1
    x[0]= x0
    while i<=(n+order):
        print("order4\n")
        y[p+1] = y[p] +(h/24)*(55*dy(x[p],y[p])-59*dy(x[p-1],y[p-1])+37*dy(x[p-2],y[p-2])-9*dy(x[p-3],y[p-3]))
        x[p+1] = x[p] + h
        print("y:"+str(i)+str(y[p+1]))

        p+=1
        i+=1



