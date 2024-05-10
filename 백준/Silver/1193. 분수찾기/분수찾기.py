x = int(input())
n = 0
tmp = 0
while True :
  tmp += 1
  n += tmp
  if n >= x :
    break

b = n-x+1
a = tmp-b+1
if tmp%2 == 0:
  print("%d/%d"%(a,b))
else :
  print("%d/%d"%(b,a))