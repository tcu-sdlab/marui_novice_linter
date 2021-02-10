n = int(input())

print('? 1 2')
S1S2 = int(input())

print('? 1 3')
S1S3 = int(input())

print('? 2 3')
S2S3 = int(input())

n1 = (S1S2 + S1S3 - S2S3) // 2
n2 = S1S2 - n1
n3 = S1S3 - n1
mas = [n1, n2, n3]


for i in range(4, n+1):
	print('? 1 ' + str(i))
	dt = int(input())
	mas.append(dt-n1)
print('!', end=' ')
for i in mas:
	print(i, end = ' ')