import heapq
n = int(input())
commands = []
arr = []
for i in range(n):
    s = input()
    tmp = s.split(' ')
    if tmp[0] == "insert":
        heapq.heappush(arr, int(tmp[1]))
    elif tmp[0] == "removeMin":
        if not len(arr):
            commands.append("insert 1")
        else:
            heapq.heappop(arr)
    else:
        x = int(tmp[1])
        while len(arr) and arr[0] < x:
            commands.append("removeMin")
            heapq.heappop(arr)
        if not len(arr) or arr[0] != x:
            commands.append("insert " + tmp[1])
            heapq.heappush(arr, x)
    commands.append(s)
print(len(commands))
print('\n'.join(commands))