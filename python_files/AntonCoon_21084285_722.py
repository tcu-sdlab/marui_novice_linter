n = int(input())
pattern = list(map(int, input().split()))
data = []
for i in range(n):
	data.append(input())
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
trigger = True
for i in range(n):
	count = 0
	for ch in data[i]:
		if ch in vowels:
			count += 1
	if count != pattern[i]:
		trigger = False
		break
if trigger:
	print('YES')
else:
	print('NO')