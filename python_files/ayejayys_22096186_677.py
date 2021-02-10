from math import ceil
n, h, k = [int(x) for x in input().split(' ')]
arr = [int(x) for x in input().split(' ')]
time = 0
i = 0
current_sum = 0
while i < n:
    while i < n and current_sum+arr[i] <= h:
        current_sum += arr[i]
        i+=1
    if i < n:
        diff = current_sum - (h - arr[i])
        curr_time = ceil(diff/k)
        time += curr_time
        current_sum = (current_sum - curr_time*k) if curr_time*k <= current_sum else 0
    else:
        time += ceil(current_sum/k)
print(time)