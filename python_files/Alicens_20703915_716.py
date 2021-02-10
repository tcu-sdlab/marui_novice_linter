n = int(input())

x = 2

for i in range(1, n+1):
    k = i**3  + 2 * (i ** 2) + i - x//i;

    print(k)

    x = x + k * i;
    x = round(x**0.5)