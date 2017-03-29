# http://nextline.tistory.com/118
from pwn import *
from re import *

s = remote("pwnable.kr" ,9007)
count = 0

def coininput(st, end):
	global count
	num = ""
	sub = end - st

	if end - st == 1:
		s.sendline(str(end-1))
		count += 1
		print "[+] Found " + str(count) +" coins!"
		return -1, -1

	for i in range(st, st + (sub/2)):
		num += str(i) + " "
	s.sendline(num)
	csum = int(s.recv(1024))

	return csum, st + (sub/2)

def set():
	find = s.recv(1024)
	data = findall("([0-9]{1,3})",find)

	N = int(data[0])
	C = int(data[1])
	print "[+] N = " + str(N) + ", C = " + str(C)

	return N

s.recvuntil('... -\n\t\n')
print "[+] Wait 3 Second..."
st, end = 0, set()


while True:
	csum, end_2 = coininput(st, end)

	if csum == -1 and count < 100:
		s.recvuntil('N')
		st, end = 0, set()
		continue
	elif csum == -1 and count >= 100:
		s.interactive()
		break

	if csum % 10 == 0:
		st = end_2
	else:
		end = end - (end - st)/2
