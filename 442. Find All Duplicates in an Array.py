class Solution:
    def findDuplicates(self, N: List[int]) -> List[int]:
        '''s, A = set(), []
        for n in N:
            if n  in s: A.append(n)
            else:
                s.add(n)
                    
        return A '''
        return [key for key,value in collections.Counter(N).items() if value == 2]
