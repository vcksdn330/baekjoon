import sys

S =[]
AS = [i for i in range(1,21)]
m = int(input())

for _ in range(m) :
    r = sys.stdin.readline().split()
    if len(r) == 2 :
        num = int(r[1])
    if r[0] == "all" :
        S.clear()
        for i in range(20) :
            S.append(AS[i])
    elif r[0] == "add" :
        if S.count(num) == 0 :
            S.append(num)
    elif r[0] == "remove" :
        if S.count(num) > 0 :
            S.remove(num)
    elif r[0] == "check" :
        sys.stdout.write("%d\n" %S.count(num))
    elif r[0] == "toggle" :
        if S.count(num) == 1 :
            S.remove(num)
        else :
            S.append(num)
    else :
        S.clear()
