class Solution:
    def findComplement(self, num: int) -> int:
        a=bin(num)[2:]
        print(a)
        s=''
        for i in a:
            if i=='0':
                s=s+'1'
            elif i=='1':
                s=s+'0'
        print(s)
        c=int(s,2)
        return (c)
        
