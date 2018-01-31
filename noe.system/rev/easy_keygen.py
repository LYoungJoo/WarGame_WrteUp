nickname = '*EBs]_M;qwOp&'
a1 = [0 for i in range(len(nickname))]

for i in range(len(nickname)):
	print i
	if i % 2 == 1:
		a1[i] = chr((i ^ (ord(nickname[i])-i)))
	else :
		a1[i] = chr(i ^ ord(nickname[i]))

print "".join(a1)
