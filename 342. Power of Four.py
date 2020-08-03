class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        '''if n==0:
			return False
		while(n%4==0):
			n = n/4
		if (n==1):
			return True
		return False '''
        if num<1:
            return False
        x = log(num)/log(4) 
        #log4( a ) = logX( a ) / logX( 4 ), where"X" can be any number
        return  x == int(x)
    '''
        if num < 0:
            return False
        
        binary = bin(num).replace('0b','')
        count_1 = binary.count('1')
        count_0 = binary.count('0')
        
        if count_1 == 1 and count_0 %2 == 0:
            return True
        
        return False ''' 
    '''
        if n<=0: return False
		return n&(n-1)==0 and (n-1)%3==0
        '''
