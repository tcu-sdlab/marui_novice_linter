money, change = list(map(int, input().split()))
i = 1
while True:
    if money*i % 10 == 0 or money*i % 10 == change:
        print(i)
        break
    i += 1