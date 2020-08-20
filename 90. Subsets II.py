class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        a=[[]]
        nums.sort()
        for i in nums:
            a+=[b+[i] for b in a]
        b=[]
        a.sort()
        for i in a:
            if i not in b:
                b.append(i)
        return b
