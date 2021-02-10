def A():
	n = int(input())
	
	if n == 1:
		item = int(input())
		if item == 0:
			print("UP")
		elif item == 15:
			print("DOWN")
		else:
			print("-1")
		return 0
	else:
		lst = [int(x) for x in input().split()]
	
	if lst[-2] > lst[-1] and lst[-1] != 0:
		print("DOWN")
	elif lst[-2] > lst[-1]:
		print("UP")
	elif lst[-2] < lst[-1] and lst[-1] != 15:
		print("UP")
	else:
		print("DOWN")
	return 0
	
if __name__ == "__main__":
	A()