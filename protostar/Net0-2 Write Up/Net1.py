# using pwntool : https://github.com/Gallopsled/pwntools
from pwn import *

s = remote('10.211.55.9', 2999)

data = int(s.recvline()[13:22])

print "[+] RECV " + str(data)
print "[+] SEND"

s.send(p32(data))
print "[+] " + str(s.recvline())
