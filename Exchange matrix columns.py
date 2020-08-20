#code
for _ in range(int(input())):
    m,n=map(int,input().split())
    k=list(map(int,input().split()))
    a=[]
    b=[]
    z=[]
    p=0
    for i in range(m):
        for j in range(n):
            a.append(k[p])
            p+=1
        b.append(a)
        a=[]
    for i in b:
        i[0],i[-1]=i[-1],i[0]
    for i in b:
        for j in i:
            z.append(j)
    print(*z)
            
