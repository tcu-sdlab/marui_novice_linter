s = input()
q = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
qt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
counts = {x : 0 for x in q}
counts['?'] = -26

if len(s) < 26:
    print(-1)
    exit()

# char counted
for i in s[:26]:
    counts[i] += 1

# first slice is correct?
if max(counts.values()) < 2:
    cur_slice = s[:26]

    for i in cur_slice:
        qt = qt.replace(i, '')

    for i in cur_slice:
        if i != '?':
            print(i, end='')
        else:
            temp = qt[0]
            qt = qt.replace(temp, '')
            print(temp, end='')
    print(s[26:].replace('?', 'A'))

    exit()


# fwd
shift = 1
while shift + 26 <= len(s):

    cur_slice = s[shift:shift + 26]

    # dec first char
    counts[s[shift - 1]] -= 1
    # inc new char
    counts[cur_slice[-1]] += 1

    # correct slice
    if max(counts.values()) < 2:

        for i in cur_slice:
            qt = qt.replace(i, '')

        print(s[:shift].replace('?', 'A'), end='')
        for i in cur_slice:
            if i != '?':
                print(i, end='')
            else:
                temp = qt[0]
                qt = qt.replace(temp, '')
                print(temp, end='')
        print(s[shift + 26:].replace('?', 'A'), end='')
        exit()


    shift += 1

print(-1)