def powerSet(s):
    res = ['']
    for i in s:
        res = [x+i for x in res]+res
        print(res)
    return res
print(powerSet('abc'))
