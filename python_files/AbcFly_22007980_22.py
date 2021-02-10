n = int(input());
s = set(map(int,input().split()));
if len(s)<2:
    print('NO');
else:
    print(sorted(list(s))[1]);