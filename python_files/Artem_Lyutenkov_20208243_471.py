s = sorted(int(x) for x in input().split())
for i in range(3):
    if s[i] == s[i + 3]:
        s[i:i + 4] = []
        print('Elephant' if s[0] == s[1] else 'Bear')
        exit()
print('Alien')