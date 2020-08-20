class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s=bin(n)[2:]
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                return 0
        return 1
        
            
        
