n = int(input())
com = [[] for i in range(n+1)]
p = int(input())
for i in range(p) :
    a,b = map(int, input().split())
    com[a].append(b)
    com[b].append(a)
queue = [1]
num = -1
while queue :
    num += 1
    x = queue.pop(0)
    for i in com[x] :
        com[i].remove(x)
        if i not in queue :
            queue.append(i)

print(num)