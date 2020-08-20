class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def helper(curr, idx):
            if sum(curr) > target:
                return  
            if sum(curr) == target:
                res.append(curr)
                return  

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue

                helper(curr + [candidates[i]], i+1)

        helper([], 0)

        return res
        
