ary = sorted([int(i) for i in input().split()])
s = 0
for i in ary:
	s += abs(i - ary[1])
print(s)