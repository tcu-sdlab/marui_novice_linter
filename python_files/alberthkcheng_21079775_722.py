import re

ans = "YES"
regex = re.compile("([aeiouy][^aeiouy]*)|([^aeiouy]*[aeiouy ])")

n = int(input())
p = list(map(int,input().split(" ")))

for i in range(n):
	temp = input()
	count = 0
	# print("Temp: ", temp)
	for m in regex.finditer(temp):
		sp = m.span()
		# print(temp[sp[0]:sp[1]])
		if re.search("[aeiouy]", temp[sp[0]:sp[1]]):
			count += 1
	# print(count)
	# print(p[i])
	# print(count != p[i])
	if count != p[i]:
		ans = "NO"
		break


print(ans)