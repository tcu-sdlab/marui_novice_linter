n, k = [int(i) for i in input().split()]

ary = []

for i in range(n):
	ary.append(input())

key = input()

def allSum(n):
	return n * 1 + (n // k) * 5

def worstSum(n):
	if n % k != 0:
		return n * 1 + (n // k) * 5
	return n * 1 + (n // k - 1) * 5

smaller = 0
equal = 0

for i in ary:
	if len(i) < len(key):
		smaller += 1
	if len(i) == len(key):
		equal += 1

print(
	allSum(smaller) + 1
	)

print(
	worstSum(smaller + equal) 
	)