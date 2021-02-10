number1,number2=map(int,input().split())
ara=[]
while number2>number1:
	if number2%10==1:
		ara.append(number2)
		number2=int(number2/10)
	elif number2%2==1:
	    break
	else:
		ara.append(number2)
		number2=int(number2/2)
ara.append(number2)
if number2==number1:
	print("YES")
	print(len(ara))
	for i in ara[::-1]:
		print(i,end=' ')
else:
	print("NO")