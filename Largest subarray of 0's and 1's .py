def maxLen(arr):
    # code here
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=-1
    sum=0
    maxi=0
    d={}
    for i in range(len(arr)):
        sum=sum+arr[i]
        if sum==0:
            maxi=i+1
        if sum in d:
            maxi=max(i-d[sum],maxi)
        else:
            d[sum]=i
    return maxi
