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
a=[4, 6, 12, 24, 30]
#for i in str(n):
    #a.append(i)
print(*abc(a))

