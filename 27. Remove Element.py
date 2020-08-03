class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=nums.count(val)
        while(n):
            if val in nums:
                nums.remove(val)
            else:
                return nums
            n-=1
        
