n = int(input())
flag = False
for i in range(n):
	t,a,b=input().split()
	if int(a) >= 2400 and int(b) > int(a) : flag = True
if flag:
    print("YES")
else: 
    print("NO")