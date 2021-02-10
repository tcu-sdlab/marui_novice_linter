#(one,one,one) or (two(any of 3),one)
#x is for (one,one,one) and pair of color is for (two(any of 3),one)
#As the don't depend on position and internal distribution
r,g,b=map(int,input().split())
x=int((r+b+g)/3)
print(min(x,r+g,r+b,b+g))