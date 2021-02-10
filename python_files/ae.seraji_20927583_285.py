n = int(input())
ary = [int(i) for i in input().split()]
ary.sort()

out = 0
c = 0
for i in ary:
	c += 1
	out += abs(i - c)

print(out)