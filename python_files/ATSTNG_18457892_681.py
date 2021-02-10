parse_int = lambda x=input: list(map(int, x().split()))

#mtx = [ [0 for _y in range(10) ] for _x in range(10) ]


partis = [input().split() for _ in range(int(input()))]

for _ in range(len(partis)):
    if int(partis[_][1])>=2400 and int(partis[_][2])>int(partis[_][1]):
        print('YES')
        quit()


print('NO')