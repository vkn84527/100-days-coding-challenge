class Solution:
    def combinationSum(self, candidates: List[int], target: int) :
        def dfs(curr, nums):       
            
            if(sum(curr) > target):                             
                return
            
            if(sum(curr) == target):
                #answer found
                result.append(curr[:])
                return
            
            for i in range(len(nums)):
                dfs(curr + [nums[i]], nums[i:])          
        result = []
        dfs([], candidates)
        return result
