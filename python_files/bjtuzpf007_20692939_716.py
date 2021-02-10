cnt, batch = input().split()
cnt = int(cnt)
batch = int(batch)
times = list(map(int, input().split()))
flag = 1
for i in range(len(times) - 1):
    if times[-i - 1] - times[-i - 2] > batch:
        flag = 0
        break
if flag:
    print(len(times))
else:
    print(i + 1)