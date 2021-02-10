def prime(c):
    i = 2
    while i * i < c:
        if c % i == 0:
            return 0
        i += 1
    return 1

ans = 0
cnt = 0
i = 2
for i in (list(range(2, 50))):
    if prime(i):
        print(i, flush=True)
        ans += (1 if input().strip() == 'yes' else 0)
        cnt += 1
    i += 1
if ans >= 2:
    print("composite", flush=True)
else:
    print("prime", flush=True)