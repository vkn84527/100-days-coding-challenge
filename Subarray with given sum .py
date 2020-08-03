li=[1,4,20,3,10,5]
su=33
lis=[]
N=len(li)
for i in range(N):
    sums=0
    for j in range(i,N):
        sums=sums+li[j]
        if sums==su:
            lis=[i,j]
            print(lis)
        if sums>su:
            break
        
    
