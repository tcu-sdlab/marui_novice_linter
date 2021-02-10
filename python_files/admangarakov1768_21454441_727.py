a = input()
s = []
T = 'NO'
b = 0



b = a[a.find(' ')+1:]
a = a[0:a.find(' ')]

a = int(a)
b = int(b)

s.append(b)
new_s = ''
#print(a)
#print(b)
#
try:
    if((b<=1000000000)and(b>a) and (a>=1)):
        for i in range(a,b):
            if(b%2 != 0):
                b = (b - 1)/10
                s.append(b)
            elif(b%2 == 0):
                b = b / 2
                s.append(b)
            if(b<a):
                T = 'NO'
                break
            if(b == a):
                T = 'YES'
                break
        if(T == 'YES'):
            s.reverse()
            print(T)
            print(len(s))
            for element in s:
                new_s = new_s + str(int(element)) + ' '
            print (new_s[:len(new_s)-1])
        else:
            print(T)
    new_s = ''
    s = []
    T = ''
    b = 0
except(TypeError, ValueError):
    print()