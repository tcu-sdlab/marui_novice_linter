a = int (input ());
b = input ().split ();
error = 0;
if (b [a - 1] == "0"):
    print ("UP");
    error = 1;
if (b [a - 1] == "15"):
    print ("DOWN");
    error = 1;
if ((a == 1) and (error == 0)):
    print ("-1");
    error = 1;
if (error == 0):
    if (int (b [a - 1]) < int (b [a - 2])) :
        print ("DOWN");
    else:
        print ("UP");