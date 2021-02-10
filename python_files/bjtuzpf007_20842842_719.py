num = input()
record = list(map(int, input().split()))
if record[-1] == 15:
    print('DOWN')
elif record[-1] == 0:
    print('UP')
elif len(record) == 1:
    print(-1)
elif (record[-1] - record[-2]) > 0:
    print('UP')
else:
    print('DOWN')