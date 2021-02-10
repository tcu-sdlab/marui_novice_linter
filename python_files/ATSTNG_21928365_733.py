from queue import PriorityQueue

fmap = lambda f,l: list(map(f,l))
parse_int = lambda: fmap(int, input().split())

pri, cur = 1, 1
son = 'AEIOYU'
for let in input().strip()+'O':
    if let in son:
        cur = 1
    else:
        cur += 1
        pri = max(cur, pri)

print(pri)