a, b, c = [int(x) for x in input().split(' ')]
x = c//b
possible = False
for i in range(0, x+1):
    if (c-i*b)%a == 0:
        possible = True
        break
print("Yes" if possible else "No")