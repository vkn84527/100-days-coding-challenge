class Solution:
    def generate(self, n: int) -> List[List[int]]:
        a,b,c=[1],0,[]
        while b<n:
            c.append(a)
            a=[1]+[a[i]+a[i+1] for i in range(len(a)-1) ]+[1]
            b+=1
        return c
        
