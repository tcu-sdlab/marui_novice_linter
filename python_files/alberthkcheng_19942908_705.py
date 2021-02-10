[n, q] = list(map(int, input().split(" ")))

total_cell = [0] * n
max_2 = [0] * n
max_3 = 0
message = []
total = 0
time = 0

ans = ""

for i in range(q):
    [t, x_t] = list(map(int, input().split(" ")))
    
    if t == 1:
        total_cell[x_t-1] += 1
        message.append(x_t)
        total += 1
    elif t == 2:
        total -= total_cell[x_t-1]
        total_cell[x_t-1] = 0
        max_2[x_t-1] = len(message)
    else:
        for j in range(max_3, x_t):
            if j >= max_2[message[j]-1]:
                total_cell[message[j]-1] -= 1
                total -= 1
        max_3 = max(max_3, x_t)
        
    ans += (str(total)+'\n')
    # print(total_cell)
    # print(total)  

print(ans)