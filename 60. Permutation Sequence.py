from itertools import permutations
class Solution:
    def getPermutation(self, n,k):
        return ''.join(str(e) for e in list(permutations(range(1, n+1)))[k-1])
        
        
        
