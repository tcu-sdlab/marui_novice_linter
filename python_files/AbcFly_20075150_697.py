t,s,x = map(int,input().split())
if x==t or (x>=t+s and (x-t)%s<=1):
    print("YES")
else:
    print("NO")