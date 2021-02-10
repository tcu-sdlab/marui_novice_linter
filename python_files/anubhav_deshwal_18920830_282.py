ip = input()
it=int(ip)
temp = 0
res = 0
while temp<it:
    st = input()
    if st == 'X++' or st == '++X':
        res+=1
    else:
        res-=1
    temp+=1
print(res)