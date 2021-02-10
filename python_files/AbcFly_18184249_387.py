sh,sm = map(int,input().split(":"))
ts,tm = map(int,input().split(":"))
rm = sm - tm
if rm<0:
    rm+=60
    ts+=1
rh = (sh - ts + 24)%24
print("%02d:%02d" % (rh,rm))