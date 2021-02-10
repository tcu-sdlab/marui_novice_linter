def vowel(s):
    b=0
    a=["a","i","o","u","y","e"]
    for i in range(len(s)):
        if s[i]==a[0] or s[i]==a[1] or s[i]==a[2] or s[i]==a[3] or s[i]==a[4] or s[i]==a[5]:
            b+=1
    return b
n=int(input())
l=list(map(int,input().split()))
q=[]
j="YES"
for i in range(n):
    if (vowel(input())!=l[i] ):
        j="NO"
        
print(j)