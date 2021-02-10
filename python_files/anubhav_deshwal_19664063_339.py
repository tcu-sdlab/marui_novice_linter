st=input().split("+")
st=[int(i) for i in st]
n1=st.count(1)
n2=st.count(2)
n3=st.count(3)
total=n1+n2+n3
for i in range(0,total):
    if n1 != 0:
        print(1,end='')
        n1-=1
    elif n2 != 0:
        print(2,end='')
        n2-=1
    elif n3 != 0:
        print(3,end='')
        n3-=1
    if i < total-1:
        print('+',end='')