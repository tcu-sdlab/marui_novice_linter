sl="";
for i in range(3):
    sl+=input();
print(['NO','YES'][sl==sl[::-1]]);