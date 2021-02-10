s1,s2 = input().split("|")
s3 = input()
m1 = len(s1)
m2 = len(s2)
m3 = len(s3)
m4 = abs(m1-m2)
if (m3-m4)>=0 and (m4-m3)%2==0:
    index = (m4+m3)//2
    if m1>m2:
        print(s1+s3[index:]+"|"+s2+s3[:index])
    else:
        print(s1+s3[:index]+"|"+s2+s3[index:])
else:
    print("Impossible")