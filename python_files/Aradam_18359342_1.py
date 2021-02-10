n, m, a = input ().split ();
n = int (n);
m = int (m);
a = int (a);
x = n // a;
if (n % a != 0):
    x += 1;
y = m // a;
if (m % a != 0):
    y += 1;
print (x * y);