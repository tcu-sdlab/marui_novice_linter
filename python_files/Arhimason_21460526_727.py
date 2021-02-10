inpt = input()
string = inpt + 'z'

number = ''
summa = 0
for i in string:
	if i.isdigit() or i == '.':
		number += i
	elif number:
		splo = number.split('.')
		if len(splo)>1:
			if len(splo[-1])==2:
				number = number[:-3].replace('.', '') + '.' + splo[-1]
			else:
				number = number.replace('.', '')
		summa += float(number)
		number = ''



dop = 0
wStr = str(round(summa,2))
if wStr[-2:-1] == '.': 
	if wStr[-1] == 0:
		wStr = wStr[:-2]
	else:
		wStr += '0'

if '.' in wStr:
	dop = wStr[-3:]
	if dop == '.00': dop = ''
	wStr = wStr[:-3]
	ln = len(wStr)
else:
	ln = len(wStr)

nvar = 4 - ln % 3
readyStr = ''
for i in range(ln):
	readyStr += wStr[i]
	if (i+nvar) % 3 == 0 and i != ln-1: readyStr += '.'

if dop: readyStr += dop

print(readyStr)