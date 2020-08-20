from itertools import combinations 
  
# Get all permutations of [1, 2, 3] 

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        a=[]
        for i in range(1,n+1):
            a.append(i)
        perm = list(combinations(a,k))
        return perm
        
