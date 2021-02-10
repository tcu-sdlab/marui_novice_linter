input()
string = input()

k = 0
out = []
state = True if string[0] == 'B' else False
size = 0
if state == True:
	k += 1

for i in string:
	newState = True if i == 'B' else False
	if newState == state and newState == True:
		size += 1
	if newState != state and newState == True:
		k += 1
		if size != 0: out.append(size)
		size = 1
	state = newState

out.append(size)

lis = ""
for i in out:
	lis += str(i) + " "
print(k)
if k > 0:
	print(lis)