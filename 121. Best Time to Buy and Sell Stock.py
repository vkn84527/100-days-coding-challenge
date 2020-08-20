class Solution:
    def maxProfit(self, p: List[int]) -> int:
        '''a,b=float('inf'),0
        for i in p:
            a,b=min(a,i),max(b,i-a)
        return b'''
        max_pro,lowest=0,float('inf')
        for i in p:
            lowest=min(i,lowest)
            max_pro=max(max_pro,i-lowest)
        return max_pro
    
