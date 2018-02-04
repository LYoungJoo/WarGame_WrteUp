```python
rgblist = '113 145 171 40 151 163 40 143 157 154 60 122 103 60 114 50 51 162'.split()
flag = ''
for i in rgblist:
  flag += chr(int(str(i),8))
print flag
```
