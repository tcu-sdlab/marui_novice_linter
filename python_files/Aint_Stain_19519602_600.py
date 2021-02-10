import bisect
n, m = map(int,input().split())
ara1 = [int(x) for x in input().split()]
ara2 = [int(x) for x in input().split()]
ara1.sort()
for i in range(m):
    print(bisect.bisect(ara1,ara2[i]))