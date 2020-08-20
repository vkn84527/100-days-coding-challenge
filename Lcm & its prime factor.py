def abc2(a,b):
    a=int(a)
    b=int(b)
    l=max(a,b)
    s=min(a,b)
    t=l
    while(1):
        if t%s==0:
            return t
        t+=l
    
def abc(a):
    while(1):
        if(len(a)!=1):
            b=a[0]
            c=a[1]
            a.remove(a[0])
            a.remove(a[0])
            b1=abc2(b,c)
            a.append(b1)
        else:
            return a
#n=int(input())
a=[1, 2, 3, 4, 5, 6, 7, 8]
#for i in str(n):
    #a.append(i)
print("LCM of this No.",a," is : ",end=" ")
print(*abc(a))
n=abc(a)[0]
n4=n
b=[]
for i in range(2,n):
    j=i
    if i<=n:
        while(1):
            if(n%j==0):
                b.append(j)
                n=n//j
            else:
                break
    else:
        break
print("factor of this LCM ",n4,"is : ",end=" ")
print(*b)
z=b
k=set()
for i in range(len(z)):
    for j in range(2,i):
        if z[i]%j==0:
            break
    k.add(z[i])
print("Prime Factor of this ",n4,":",end=" ")
print(*k)
def hcf(a, b): 
    while (a != b): 
        if (a > b): 
            a = a - b 
        else: 
            b = b - a 
    return a
print(hcf(60,96))






            
