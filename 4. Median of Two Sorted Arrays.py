class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=(nums1+nums2)
        num.sort()
        print(num)
        if len(num)%2!=0:
            return num[len(num)//2]
        else:
            n=len(num)//2
            return (num[n]+num[n-1])/2
