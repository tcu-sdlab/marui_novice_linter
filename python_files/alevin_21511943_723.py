a, b, c = map(int, input().strip().split())

min_r_a = 1000
for i in range(1, 101):
    r_a = abs(a - i) + abs(b - i) + abs(c - i)
    min_r_a = min(r_a, min_r_a)
print(min_r_a)