# cook your dish here
from functools import *
n=int(input())
s=ss=0
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(0,len(a),1):
    s|=a[i]
for i in range(0,len(b),1):
    ss|=b[i]   

print(s+ss)