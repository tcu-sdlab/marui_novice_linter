str=input()
ab=str.count("AB")
ba=str.count("BA")
aba=str.count("ABA")
bab=str.count("BAB")
sum=ab+ba-aba-bab

if sum>=2 and ab>0 and ba>0 :
    print("YES")
else:
    print ("NO")