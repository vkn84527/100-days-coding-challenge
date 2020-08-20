class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        b=[]
        for i in nums:
            if nums.count(i)==1:
                b.append(i)
        return b
        
