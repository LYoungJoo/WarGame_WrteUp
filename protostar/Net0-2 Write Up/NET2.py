# using pwntool : https://github.com/Gallopsled/pwntools
from pwn import *
import sys

s = remote('10.211.55.9', 2997)

print "[+] RECV DATA",

data = 0
for i in range(0,4):
    sleep(0.1)
    sys.stdout.write('.')
    data += u32(s.recv(4))
sys.stdout.write('done')
print ""

print "[+] SEND"
s.sendline(str(p32(data)))

print "[+] " + s.recvline()
