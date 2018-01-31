from pwn import *

_id = list('G@ytOr!es')
_pw = list('u1|g%eHey')

for i in range(0,len(_id),2):
    _id[i] = chr(ord(_id[i]) ^ 0x1a)
    _id[i] = chr(ord(_id[i]) + 16)

for i in range(0,len(_pw)-2,2):
    _pw[i] = chr(ord(_pw[i]) ^ 0x66)
    _pw[i] = chr(ord(_pw[i]) ^ ord(_id[i+1]))

s = remote('noe.systems',51000)
s.sendlineafter('ID: ',"".join(_id))
s.sendlineafter('PW: ',"".join(_pw))
s.interactive()
