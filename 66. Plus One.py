class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in digits:
            s=s+str(i)
        return str(int(s)+1)
        
