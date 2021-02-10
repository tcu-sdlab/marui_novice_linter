st = list(input())


def printer(start, end):
    done = {}
    for al in range(ord('A'), ord('Z')+1):
        done[al] = 0

    for c in st[start:end+1]:
        done[ord(c)] = 1

    for c in st[0:start]:
        if c == '?':
            print('A', end='')
        else:
            print(c, end='')

    for c in st[start:end+1]:
        if c != '?':
            print(c, end='')
        else:
            for al in range(ord('A'), ord('Z')+1):
                if not done[al]:
                    print(chr(al), end='')
                    done[al] = 1
                    break

    for c in st[end+1:]:
        if c == '?':
            print('A', end='')
        else:
            print(c, end='')
    print()

cnt = {}
for al in range(ord('A'), ord('Z')+1):
    cnt[al] = 0

start = 0
mis = 0
have = 0
did = 0

if len(st) < 26:
    print("-1")
    raise SystemExit

for i, c in enumerate(st):
    if c == '?':
        mis += 1
    else:
        while start < i and cnt[ord(c)] != 0:
            if st[start] == '?':
                mis -= 1
            else:
                cnt[ord(st[start])] = 0
                have -= 1
            start += 1
        cnt[ord(c)] = 1
        have += 1

    if have + mis == 26:
        did = 1
        printer(start, i)
        break

    # print(i, c, start, mis, have)

if not did:
    print("-1")