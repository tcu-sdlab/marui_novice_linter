n = int(input())

ALLL = 0
ALLR = 0

MLP = 0
MRP = 0
MLPI = 0
MRPI = 0

for i in range(n):
	inp = input().split()
	L = int(inp[0])
	R = int(inp[1])
	ALLL += L
	ALLR += R
	LP = R - L
	RP = L - R

	if LP>MLP: 
		MLP = LP
		MLPI = i

	if RP>MRP: 
		MRP = RP
		MRPI = i

ML = ALLL - ALLR + 2*MLP
MR = ALLR - ALLL + 2*MRP

if ML>MR:
	if MLP == 0:
		print(0)
	else:
		print(MLPI+1)
else:
	if MRP == 0:
		print(0)
	else:
		print(MRPI+1)