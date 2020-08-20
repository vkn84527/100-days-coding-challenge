for _ in range(int(input())):
    m=int(input())
    k=list(map(int,input().split()))
    a=[]
    b=[]
    z=[]
    p=0
    c=[]
    for i in range(m):
        for j in range(m):
            a.append(k[p])
            p+=1
        b.append(a)
        a=[]
    for i in range(m):
        if i%2==0:
            c.append(b[i])
        else:
            b[i]=b[i][::-1]
            c.append(b[i])
    for i in c:
        for j in i:
            z.append(j)
    print(*z)
        
        
