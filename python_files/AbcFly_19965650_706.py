a,b = map(int, input().split())
n = int(input())
res = []
for i in range(n):
    x,y,v = map(int, input().split())
    res+=[pow((a-x)**2+(b-y)**2,0.5)/v] #计算耗时
res.sort()
print("%.8f" % res[0])