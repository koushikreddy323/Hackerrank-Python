'''
TO CALCULATE THE COUNT OF NO OF DELETIONS MADE TO GET A STRING WITHOUT SAME CHARS REPETING BESIDE
'''
def boom(s):
  i=0
  v=s[0]
  for x in s[1:]:
    if x==v:
      i+=1
    else:
      v=x
  print(i)
boom('AAABBB')
