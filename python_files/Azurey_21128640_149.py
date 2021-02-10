mum = int(input())
lst = list(map(int, input().split()))

result = 0

if sum(lst) < mum:
    print(-1)
else:
    while mum > 0:
        mum -= max(lst)
        lst.remove(max(lst))
        result += 1
    print(result)