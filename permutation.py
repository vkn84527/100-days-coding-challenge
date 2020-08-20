def abc(nums):
    if len(nums)==0:
        return []
    if len(nums)==1:
        return [nums]
    l=[]
    for i in range(len(nums)):
        m=nums[i]
        rem=nums[:i]+nums[i+1:]
        #print(m,rem,end=" ")
        for p in abc(rem):
            l.append([m]+p)
            #print(l)
    return l

print(abc([1,2,3]))
