a, b = map(int, input().split())
ls = []
for i in range(1,7):
    ls.append(abs(a-i)<abs(b-i))
x = sum(ls)
y = 1-(a-b)%2 + 5*(a==b)
print(x, y, 6-x-y)