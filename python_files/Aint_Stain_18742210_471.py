b=sorted(list(map(int, input().split())))

if b[0]==b[1]==b[2]==b[3] or b[1]==b[2]==b[3]==b[4] or b[2]==b[3]==b[4]==b[5]:
    if b[0]==b[5] or (b[0]==b[1] and b[4]==b[5]):
        print("Elephant")
    else:
        print("Bear")
else:
    print("Alien")