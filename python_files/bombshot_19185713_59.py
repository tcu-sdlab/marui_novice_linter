s=input()
c_1,c_2=0,0
for i in s:
    if i.isupper():
        c_1+=1
    else:
        c_2+=1
#print (c_1,c_2)
if c_2>=c_1:
    print (s.lower())
else:
    print(s.upper())