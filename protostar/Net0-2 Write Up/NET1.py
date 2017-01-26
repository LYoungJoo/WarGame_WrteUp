# using pwntool : https://github.com/Gallopsled/pwntools
from pwn import *

s = remote('10.211.55.9', 2998)

data = u32(s.recv(1024)) # unpacking

print "[+] RECV " + str(data)
print "[+] SEND "
s.sendline(str(data))

print "[+] " + s.recvline()
