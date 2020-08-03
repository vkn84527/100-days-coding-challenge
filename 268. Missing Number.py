class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        c=sorted(nums)
        for i in range(len(c)+2):
            if i not in c:
                return i
        
