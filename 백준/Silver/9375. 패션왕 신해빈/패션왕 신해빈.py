import sys

for _ in range(int(sys.stdin.readline())) :
    i = int(sys.stdin.readline())
    arrs = {}
    for _ in range(i) :
        e, s = sys.stdin.readline().split()
        arrs[e] = s
    
    kind = []
    count = []
    for a in arrs :
        if arrs[a] in kind :
            count[kind.index(arrs[a])] += 1
        else :
            kind.append(arrs[a])
            count.append(1)
    
    ans = 1
    for i in count :
        ans *= (i+1)
    sys.stdout.write("%d\n"%(ans-1)) 
    ###부위 count + 1 * 각부위 ... - 1