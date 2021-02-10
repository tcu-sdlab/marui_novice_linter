input_num = list(map(int, input().split()))
l1, r1, l2, r2, k = input_num
t = min(r1, r2) - max(l1, l2) + 1
if t < 0:
    t = 0
elif max(l1, l2) <= k <= min(r1, r2):
    t -= 1
print(t)