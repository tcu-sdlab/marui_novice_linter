p = {'K': 0, 'Q': 9, 'R': 5, 'B': 3, 'N': 3, 'P': 1, '.': 0}
w = [0, 0]
for r in range(8):
    for c in input():
        if c != '.':
            w[c.islower()] += p[c.upper()]
if w[0] == w[1]:
    print('Draw')
else:
    print('White' if w[0] > w[1] else 'Black')