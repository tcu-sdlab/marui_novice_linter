n,m = map(int, input().split(" "))

is_color = False

for i in range(n):
	pixels = input().split(" ")
	for pixel in pixels:
		if pixel in ["C", "M", "Y"]:
			is_color = True
			break

	if is_color == True:
		break

if is_color == True:
	color = "#Color"
else:
	color = "#Black&White"

print(color)