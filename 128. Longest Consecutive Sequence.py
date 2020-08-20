class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        nums.sort()
        s=set(nums)
        ls=0
        for i in nums:
            current=1
            while i+1  in s:
                i=i+1
                current+=1
            ls=max(ls,current)
        return ls
                
            
        
