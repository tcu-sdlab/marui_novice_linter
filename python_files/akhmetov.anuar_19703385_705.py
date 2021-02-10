t = input
p = print
r = range
n = int(t())
a = list(map(int, t().split()))
current_winner = 1 if a[0] & 1 == 0 else 2
p(current_winner)
for i in r(1, n):
    local_winner = 1 if a[i] & 1 == 0 else 2

    if current_winner == 1:
        if local_winner == 1:
            current_winner = 2
    else:
        if local_winner == 1:
            current_winner = 1
    p(current_winner)