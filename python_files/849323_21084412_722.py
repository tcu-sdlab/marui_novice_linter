n = int(input())
s = input()

h,m = [int(i) for i in s.split(':')]

u = h
if m not in range(0,60):
    m = m%10

if m in range(0,10):
    m = '0' + str(m)

if  h in range(0,10):
    h = '0' + str(h)
else:
    h = str(h)

if n ==12:
    if u not in range(1,13):
        h = list(h)
        if h[0] =='0':
            h[1] = '1'
        elif h[0] == '1':
            h[1] = '2'
        else:
            if h[1] == '0':
                h[0] = '1'
            else:
                h[0] = '0'
        h = "".join(h)
else:
    if u not in range(0,24):
        h = list(h)
        if h[0] =='2':
            h[1] = '2'
        else:
            h[0] ='1'
        h = "".join(h)

print("{}:{}".format(h,m))