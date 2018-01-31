from ctypes import *
from pwn import *

libc = cdll.LoadLibrary('/lib/x86_64-linux-gnu/libc.so.6')
s = remote('noe.systems', 51001)

libc.srand(1)
for i in range(32):
    libc.rand()

for i in range(119):
    print "STAGE " + str(i)
    datalist = []

    for j in range(32):
        datalist.append(libc.rand() % 255 ^ 0x77)

    s.recvuntil('INPUT: ')

    for j in datalist:
        s.sendline(str(j))

s.interactive()
