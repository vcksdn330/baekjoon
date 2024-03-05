import sys
from collections import deque

for _ in range(int(sys.stdin.readline())) :
    numlist = [0 for i in range(10000)]
    queue = deque()
    l, r = map(int, sys.stdin.readline().split())
    oa = l
    ob = r

    queue.append([oa,''])
    while queue :
        f,m = queue.popleft()
        #R
        s = f
        tmp = s%10
        s //= 10
        s += tmp * 1000
        if s == ob :
            sys.stdout.write("%sR\n"%m)
            break
        if numlist[s] == 0 :
            numlist[s] += 1
            queue.append([s,m+'R'])
        #L
        s = f
        tmp = s // 1000
        s = (s - 1000*tmp) *10
        s += tmp
        if s == ob :
            sys.stdout.write("%sL\n"%m)
            break
        if numlist[s] == 0 :
            numlist[s] += 1
            queue.append([s,m+'L'])

        #S
        s = f
        if s == 0 :
            s = 9999
        else :
            s -= 1

        if s == ob :
            sys.stdout.write("%sS\n"%m)
            break
        if numlist[s] == 0 :
            numlist[s] += 1
            queue.append([s,m+'S'])

        #D
        s = f
        s = (s*2) % 10000
        if s == ob :
            sys.stdout.write("%sD\n"%m)
            break
        if numlist[s] == 0 :
            numlist[s] += 1
            queue.append([s,m+'D'])

#first. 일단 DSLR 다 진행시켜

#third, 답 없으면 다시 전부다 DSLR 시켜. 단 앞에서 나왔던 숫자가 나오면 지워