n=int(input())
c=0;x=0;y=0;
if n==1 or n==2 : print('1')
else:
        for i in range(n):
                c+=i;x+=c;y=i
                if x>n:break       
        print(y-1)