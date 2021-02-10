n = int(input())
a = input().split()
b = sorted([(int(a[i]), i + 1) for i in range (n)])
for i in range (int(n / 2)):
    print (b[i][1], b[-i - 1][1])