from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        a=list(permutations(nums))
        return (list(set(a)))
        
