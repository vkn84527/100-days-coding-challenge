
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for ele in nums:
            result += [entry + [ele] for entry in result]
        return result
