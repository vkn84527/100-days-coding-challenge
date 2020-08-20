class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        b=[]
        a=len(nums)//3
        nums2=set(nums)
        for i in nums2:
            if nums.count(i)>a:
                b.append(i)
        return b
        
