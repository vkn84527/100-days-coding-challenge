class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        spo=[]
        while m and m[0]:
            if m[0]:
                spo+=m.pop(0)
            if m and m[0]:
                for i in m:
                    spo.append(i.pop())
            if m and m[-1]:
                spo+=m.pop()[::-1]
            if m and m[0]:
                for i in m[::-1]:
                    spo.append(i.pop(0))
        return spo
        
