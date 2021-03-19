
#Bairstow Method

import numpy as np
n = int(input("Degree of polynomial"))
p = float(input("P value"))
q = float(input("q value"))
no_iterations = int(input("number of iterations"))


a = np.zeros((n+2,1))
b = np.zeros((n+2,1))
c = np.zeros((n+2,1))
j = n+1


for i in range(n+1):
    a[i] = float(input("Enter coefficients of a:"))

for x in range(no_iterations):
    #setting initial values for b:
    b[0]= 0
    b[1]=a[0]

    for k in range(n+2):
        if k==0 or k==1:
            pass
        else:
            b[k]=a[k-1]-(p*b[k-1])-(q*b[k-2])

    #setting initial values for c:
    c[0]= 0
    c[1]=b[1]

    for m in range(n+2):
        if m==0 or m==1:
            pass
        else:
            c[m]=b[m]-(p*c[m-1])-(q*c[m-2])


    print("a:\n")
    print(np.transpose(a) ) 
    print("\n")

    print("-p*b\n")
    print(-p*np.transpose(b)) 
    print("\n")

    print("-q*b\n")
    print(-q*np.transpose(b) )
    print("\n")


    print("b:\n")
    print(np.transpose(b) )
    print("\n")

    print("-p*c\n")
    print(-p*np.transpose(c) )
    print("\n")

    print("-q*c\n")
    print(-q*np.transpose(c) )
    print("\n")

    print("c:\n")
    print(np.transpose(c) )
    print("\n")

    print("dp=")
    dp = ((b[j-1]*c[j-2])-b[j]*c[j-3])/((c[j-2]*c[j-2])-c[j-3]*(c[j-1]-b[j-1]))
    print(dp )
    print("\n")


    print("dq=")
    dq = ((b[j]*c[j-2])-b[j-1]*(c[j-1]-b[j-1]))/((c[j-2]*c[j-2])-c[j-3]*(c[j-1]-b[j-1]))
    print(dq )
    print("\n")

    p = p + dp
    q = q + dq

    print("newp=")
    print(p )
    print("\n")

    print("newq=")
    print(q )
    print("\n")
    print("____________next iteration__________________")
    print("\n")


