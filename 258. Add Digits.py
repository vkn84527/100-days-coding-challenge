class Solution:
    def addDigits(self, num: int) -> int:
        s=0
        while(len(str(num))!=1):
            for i in str(num):
                s=s+int(i)
            num=s
            s=0
        return num
