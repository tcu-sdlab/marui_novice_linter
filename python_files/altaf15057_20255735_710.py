S=input()
x=S[0]
y=S[1]
if((x=='a' and y=='1') or (x=='h' and y=='1') or (x=='h' and y=='8') or (x=='a' and y=='8')):
    print("3")
elif((x=='a') or (x=='h') or (y=='1') or (y=='8')):
    print("5")
else:
    print("8")