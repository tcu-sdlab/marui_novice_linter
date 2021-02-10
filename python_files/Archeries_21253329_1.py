n, m, a = input().strip().split()
n = int(n)
m = int(m)
a = int(a)
print(((n - 1) // a + 1) * ((m - 1) // a + 1))