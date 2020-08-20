class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(m)
        n1=len(m[0])
        s=set()
        s1=set()
        for i  in range(n):
            for j in range(n1):
                if m[i][j]==0:
                    s.add(i)
                    s1.add(j)
        for i in s:
            for j in range(n1):
                m[i][j]=0
        for i in s1:
            for j in range(n):
                m[j][i]=0
        
