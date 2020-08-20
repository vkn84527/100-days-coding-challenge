
import numpy as np
for _ in range(int(input())):
    n=int(input())
    k=list(map(int,input().split()))
    a=[]
    b=[]
    p=0
    for i in range(n):
        for j in range(n):
            a.append(k[p])
            p+=1
        b.append(a)
        a=[]
    a1 = np.array(b) 
    print (int(round(np.linalg.det(a1))))
