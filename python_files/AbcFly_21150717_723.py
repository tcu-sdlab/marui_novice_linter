import re
input()

sl = input()
fp = False
wc = 0
ol = []
ml = [0]
while sl.count("("):
    t = sl[sl.index("("):sl.index(")")+1]
    ol+=re.split("[_()]", t)
    sl=sl.replace(t, "_",1)
for s in sl.split("_"):
    ml.append(len(s))
for o in ol:
    if o!='':
        wc+=1
print(max(ml),wc)