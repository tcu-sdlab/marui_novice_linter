tmp  = input()
n = int(tmp[:-1])
r = tmp[-1]
map = {
    'f':1,
    'e':2,
    'd':3,
    'a':4,
    'b':5,
    'c':6
}
print(((n-1)//4)*16+((n+1)%2)*7+map[r])