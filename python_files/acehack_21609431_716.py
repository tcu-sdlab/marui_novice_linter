n = int(input())

sc = 2
l = 1
k = 2

for l in range(1, n+1):
    # print(l, k, k*l)
    if k % l == 0:
        print(k**2 * l + (k**2)//l + 2*(k**2) - k)
        # print(((k**2)*((l+1)**2) - k*l)//l)
    else:
        oldk = k
        k = (k//l * l + l)
        print(k**2 * l + (k**2)//l + 2*(k**2) - oldk)