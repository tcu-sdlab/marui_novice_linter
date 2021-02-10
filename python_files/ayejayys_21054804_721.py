def find_pos(correct_len, len_list):
    pos = 0
    for i in range(correct_len):
        pos += len_list[i]
    return (pos+1, pos+len_list[correct_len]) #in 0-index mode

def find_time(pos, k):
    pauses = int((pos-1)/k)
    return pauses*5+pos

N = 102
n, k = [int(x) for x in input().strip().split(' ')]
l = [0] * N
for x in range(n):
    l[len(input().strip())] += 1
correct_len = len(input().strip())
best_pos, worst_pos = find_pos(correct_len, l)
print("%d %d" % (find_time(best_pos,k), find_time(worst_pos, k)))