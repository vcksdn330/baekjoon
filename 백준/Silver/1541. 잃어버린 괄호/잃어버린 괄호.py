import sys
c = sys.stdin.readline()
sym = []
start = 0
num = []
last = 0
for i in range(len(c)) :
    if c[i] == "+" :
        sym.append(1)
        num.append(int(c[start : i]))
        start = i+1

    if c[i] == "-" :
        sym.append(-1)
        num.append(int(c[start : i]))
        start = i+1

num.append(int(c[start :]))

presym = 1
tmp = 0
ans = num.pop(0)
for i in sym :
    if i == -1 or (presym == -1 and i == 1) :
        tmp -= num.pop(0)
        presym = -1
    elif i == 1 :
        ans += num.pop(0)
    else :
        presym = 1
        ans += tmp
        tmp = 0
        
ans += tmp

print(ans)