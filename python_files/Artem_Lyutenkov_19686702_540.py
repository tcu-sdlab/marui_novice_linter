n, a, b = int(input()), input(), input()
ans = sum(5 - abs(abs(int(a[i]) - int(b[i])) - 5) for i in range(n))
print (ans)