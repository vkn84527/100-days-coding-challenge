class Solution:
    def maxProduct(self, a: List[str]) -> int:
        if not a:
            return 0
        b=[]
        def ab(a,b):
            for i in a:
                if i  in b:
                    return 0
            return 1
        b=[]
        for i in a:
            for j in a:

                if  i==j:
                    continue
                if(ab(i,j)):
                    b.append([len(i)*len(j)])
        if len(b)==0:
            return 0
        c=max(b)
        for i in c:
            return i

        
