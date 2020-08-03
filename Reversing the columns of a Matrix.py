#code
for _ in range(int(input())):
    m,n=map(int,input().split())
    k=list(map(int,input().split()))
    a=[]
    b=[]
    p=0
    for i in range(m):
        for j in range(n):
            a.append(k[p])
            p+=1
        b.append(a)
        a=[]
    c=[]
    d=[]
    for i in b:
        c.append(i[::-1])
    for i in c:
        for j in i:
            d.append(j)
    print(*d)
            
