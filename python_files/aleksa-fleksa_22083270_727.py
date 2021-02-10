n = int(input())
ans = '! '

print('? 1 2')
a = int(input())
print('? 2 3')
b = int(input())
print('? 1 3')
c = int(input())

x = (a + b - c) // 2
ans += str(a - x) + ' '
ans += str(x) + ' '
ans += str(b - x) + ' '

for i in range(4, n + 1):
    print('?', 2, i)
    y = int(input())
    ans += str(y - x) + ' '

print(ans)