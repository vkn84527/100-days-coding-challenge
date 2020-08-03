def firstMissingPositive(self, nums: List[int]) -> int:
        c=sorted(nums)
        #return c
        if(c==[]):
            return 1
        for i in range(1,len(c)+2):
            if i not in c:
                return i
