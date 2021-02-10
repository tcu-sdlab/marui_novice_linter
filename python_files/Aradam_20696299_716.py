n, c = input ().split ();
c = int (c);
t = input ().split ();
world_count = 1;
j = 0;
for i in t :
    if (j > 0) :
        if (int (i) - int (t [j - 1]) > c) :
            world_count = 1;
        else :
            world_count += 1;
    j += 1;
print (world_count);