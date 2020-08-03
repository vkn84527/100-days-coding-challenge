    n = int(input())
    arr = [int(i) for i in input().split()]
    ct = Counter(arr)
    found = -1
    for key, value in ct.items():
        if value > n//2:
            found = key
            break
    print(found)
