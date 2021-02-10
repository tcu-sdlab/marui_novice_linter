def leap(y):
	return (y%400==0 or (y%4==0 and y%100!=0))
y=int(input())
is_leap = leap(y)
d = 0
first = 1
while(is_leap != leap(y) or d or first):
	d+=1
	if(leap(y)): 
		d+=1
	y+=1
	d%=7
	first = 0
print(y)