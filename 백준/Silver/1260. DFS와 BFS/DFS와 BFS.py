import sys
sys.setrecursionlimit(10**5)

N, M, V = map(int, sys.stdin.readline().split())
graph1 = [[] for i in range(N+1)]
graph2 = [[] for i in range(N+1)]
ck1 = [0 for i in range(N+1)]
ck2 = [0 for i in range(N+1)]
seq = []
for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    graph1[a].append(b)
    graph1[b].append(a)
    graph2[a].append(b)
    graph2[b].append(a)

for i in range(1,N+1) :
    graph1[i].sort()
    graph2[i].sort()
    
def dfs(arr, ck, seq, v) :
    if ck[v] == 0 :
        ck[v] = 1
        seq.append(v)
        while len(arr[v]) > 0 :
            dfs(arr, ck, seq, arr[v][0])
            arr[v].pop(0)

def bfs(arr, ck, seq, queue, v) :
    queue.append(v)
    while len(queue) > 0 :
        point = queue.pop(0)
        if ck[point] == 0 :
            ck[point] = 1
            seq.append(point)
            for i in arr[point] :
                queue.append(i)            
    

dfs(graph1, ck1, seq, V)
for i in seq :
    print(i, end=" ")
print()
seq.clear()
queue = []
bfs(graph2, ck2, seq, queue, V)
for i in seq :
    print(i, end=" ")