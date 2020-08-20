class Solution:
    def getRow(self, x: int) -> List[int]:
        if x==0:
            return [1]
        a,b,c=0,[],[1]
        while a<x:
            c.append(b)
            b=[1]+[b[i]+b[i+1] for i in range(len(b)-1)]+[1]
            a=a+1
        return b 
        
