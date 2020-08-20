class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        num=[0]*n
        for i in range(n):
            num[i]=start+2*i
        print(num)
        p=0
        for i in num:
            p=p^i
        return p
        
