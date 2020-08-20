class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        p=1
        a=[]
        b=[]
        for i in range(n):
            for j in range(n):
                a.append(p)
                p=p+1
            b.append(a)
            a=[]
        #print(b)
        res=[]
        while b and b[0]:
            if b[0]:
                res+=b.pop(0)
            if b and b[0]:
                for i in b:
                    res.append(i.pop())
            if b and b[-1]:
                res+=b.pop()[::-1]
            if b and b[0]:
                for i in b[::-1]:
                    res.append(i.pop(0))
        print(res)
            
        
