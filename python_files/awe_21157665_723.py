n = int(input())
s = input()
words = 0
longest = 0
b = False
d = False
count = 0
for i in s:
	if i == '(':
		b = True
		count = 0
	if b:
		if d and (i == '_' or i == ')'):
			words += 1
			d = False
		if i != '_' and i != ')' and i != '(':
			d = True
	if not b:
		if i != '_' and i != '(' and i != ')':
			count += 1
		else:
			count = 0
	if count > longest:
		longest = count
	if i == ')':
		b = False
		count = 0
print(longest, words)