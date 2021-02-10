s=sum(map(int,input().split()))
if s%5!=0 or s==0: print('-1')
else: print(s//5)