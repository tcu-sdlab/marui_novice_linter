s = input()

s = list(s)

res = -1

for i in range(len(s)):
    if i+25<len(s):
        d ={}
        count = 0
        for j in range(i,i+26):
            if s[j] =='?':
                count +=1
            else:
                d[s[j]]=1
        #print(d,count)
        
        if count + len(d) == 26:
            for j in range(i,i+26):
                if s[j] == '?':
                    for k in range(65,91):
                        if chr(k) not in d:
                            d[chr(k)] = 1
                            s[j] = chr(k)
                            break
            res = s
            break
    if res!=-1:
        break

for i in range(len(s)):
    if s[i] =='?':
        s[i] = 'A'

if res == -1:
    print(-1)
else:   
    print("".join(res))