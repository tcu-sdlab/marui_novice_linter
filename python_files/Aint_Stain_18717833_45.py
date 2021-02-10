s=str(input())
c=int(input())
a= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
d=(c+a.index(s))%12
print(a[d])