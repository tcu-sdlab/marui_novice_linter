t = list(map(int, input().split(" ")))
t.sort()

sum1 = 0
sum2 = 0

last = 0

for i in t:
	if t.count(i) >= 3:
		sum1 = 3 * i
	if t.count(i) == 2:
		sum2 = 2 * i


print(sum(t)-max(sum1,sum2))