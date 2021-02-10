import sys


def find_min_max(l, d=None):
    #print(l)
    n = len(l)
    if n == 1:
        return (l[0], l[0])
    
    lesser = []
    greater = []
    for i in range(n//2):
        first = l[2*i]
        second = l[2*i + 1]
        
        print("? {} {}".format(first, second))
        sys.stdout.flush()
        
        answer = input()
        
        if answer == '<':
            lesser.append(first)
            greater.append(second)
        else:
            lesser.append(second)
            greater.append(first)

    if n%2 == 1:
        lesser.append(l[-1])
        greater.append(l[-1])
        
    mn = None
    mx = None
    
    if d != 'max':
        mn = find_min_max(lesser, 'min')[0]
    if d != 'min':
        mx = find_min_max(greater, 'max')[1]
    return (mn, mx)


t = input()
t = int(t)

for k in range(t):
    n = input()
    n = int(n)
    
    l = list(range(1, n+1))
    mn, mx = find_min_max(l)
    print("! {} {}".format(mn, mx))
    sys.stdout.flush()