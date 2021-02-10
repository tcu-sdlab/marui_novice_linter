banyak = int(input(''))
str = input('')
str = str.replace('(','_(_')
str = str.replace(')','_)_')
str2 = str.split('_')
dalam = False
max1 = 0
max2 = 0
for i in str2 :
	if i != '':
		#print(i)
		if i == '(' :
			dalam = True
		elif i == ')' :
			dalam = False
		elif not(dalam):
			if max1 < len(i) : max1 = len(i)
		elif dalam:
			max2 += 1
print(max1,max2)
#http://codeforces.com/contest/723/problem/B