cnt = list(map(int, input().split()))
cnt.sort()
small, middle, large = cnt

if large > middle:
    print((large - 1) * 2 - middle - small)
elif middle > small:
    print(middle - small - 1)
else:
    print(0)