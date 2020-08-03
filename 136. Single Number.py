class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=set(nums)
        for i in c:
            if(nums.count(i)==1):
                return i
        
