from collections import Counter

n, m = map(int, input().split())
nums = list(map(int, input().split()))

cnts = dict(Counter(nums))
for i in range(1, m+1):
    if i not in cnts:
        cnts[i] = 0


def minner():
    return min(cnts.items(), key=lambda x: x[1])

n //= m

res = 0
for i, num in enumerate(nums):
    if num > m or cnts[num] > n:
        for r in range(1, m+1):
            if cnts[r] < n:
                cnts[num] -= 1
                nums[i] = r
                cnts[r] += 1
                res += 1
                break

print(n, res)
print(' '.join(map(str, nums)))