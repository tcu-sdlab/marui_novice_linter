import re
n = input()
new = input()
out = [len(x) for x in re.sub(r'\(.*?\)', '_', new).split('_')]
sec = ''
for i in re.findall(r'\(\w+\)?', new):
	for j in i:
		if j == '(' or j == ')':
			sec += '_'
		else:
			sec += j
ans = 0
for i in re.split(r'_+', sec):
	if i != '':
		ans += 1
if out == []:
	print(0, ans)
else:
	print(max(out), ans)