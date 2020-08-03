from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''if len(nums)==0:
            return []
        if len(nums)==1:
            return [nums]
        l=[]
        for i in range(len(nums)):
            m=nums[i]
            rem=nums[:i]+nums[i+1:]
            for p in self.permute(rem):
                l.append([m]+p)
        return l'''
        a=list(permutations(nums))
        return a
        
