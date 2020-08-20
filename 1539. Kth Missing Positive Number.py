class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        b=[]
        for i in range(1,len(arr)+k+1):
            if i not in arr:
                b.append(i)
        print(b)
        return b[k-1]
            
            
        
