def largestNum(n,s):
    '''
    :param n: length of given numberr
    :param s: sum of digits of number
    :return: Integer
    '''
    # code here/
    p=""
    if (s>9*n):
        return -1
    else:
        for i in range(n):
            if(s>9):
                p=p+'9'
                s=s-9
            else:
                p=p+str(s)
                s=0
    return p
