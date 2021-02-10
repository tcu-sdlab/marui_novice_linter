n = int(input())
m = 5
ans = 1
for i in range(2, m+1):
    ans *= i
j = 1
for i in range(m+1, n+1):
    ans = (ans*i*i)//(j*j)
    j += 1
print(ans)