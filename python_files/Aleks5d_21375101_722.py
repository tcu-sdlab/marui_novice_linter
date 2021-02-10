count = int(input());
b = [int(i) for i in input().split()]

alp = ['a', 'e', 'y', 'u', 'i', 'o']
for i in range(count):
    s = input()
    for j in s:
        if j in alp:
            b[i]-=1;
    if b[i] != 0:
        print("NO")
        exit()
print("YES")