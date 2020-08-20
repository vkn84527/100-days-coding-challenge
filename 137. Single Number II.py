class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b=[]
        for i in nums:
            if nums.count(i)==1:
                b.append(i)
        for j in b:
            return j
        
        
