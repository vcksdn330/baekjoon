from collections import deque

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
check = [0 for i in range(n+1)]
for _ in range(m) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph,check, a) :
    q = deque()
    q.append(a)
    flag = 0
    if check[a] == 0 :
        flag = 1
        while q :
            x = q.popleft()
            check[x] = 1
            tmp = graph[x].copy()
            for i in tmp :
                q.append(i)
                graph[x].remove(i)
                graph[i].remove(x)

    if flag == 1 :
        return 1
    else :
        return 0

num = 0

for i in range(1,n + 1) :
    num += bfs(graph,check, i)

print(num)