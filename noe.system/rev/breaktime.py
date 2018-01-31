string = ['=', 'F', '=', 'o', '@', 'q', '[', ']', 'J', 'S', '=', 'c', 'w', 'E', '^', '=', '<', 'e', '_', 't']
bytelist = [ 12, 4, 7, 15, 1, 4, 9 ]

j = 5
i = 19
while i != -1:
  string[i] = chr(ord(string[i]) + 5)
  string[i] = chr(ord(string[i]) ^ bytelist[j])
  print 'i : ' + str(i) + ',j : ' + str(j)
  j -= 1
  if j == -1:
      j = 6
  i -= 1
print "".join(string)
