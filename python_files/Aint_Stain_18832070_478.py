r,g,b=map(int,input().split())
x=int((r+b+g)/3)
print(min(x,r+g,g+b,b+r))