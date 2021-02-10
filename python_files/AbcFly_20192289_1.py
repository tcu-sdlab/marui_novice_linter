n,m,a = map(int, input().split())
x = n//a + (n%a>0)
y = m//a + (m%a>0)
print(x*y)