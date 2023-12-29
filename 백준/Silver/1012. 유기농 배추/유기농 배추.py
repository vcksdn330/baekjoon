import sys
sys.setrecursionlimit(10**7)
def dfs(arr, x, y, M, N) :
    if x < 0 or x >= M or y < 0 or y >= N :
        return
    elif arr[y][x] == 0 :
        return
    arr[y][x] = 0
    dfs(arr, x, y+1, M, N) #상
    dfs(arr, x, y-1, M, N) #하
    dfs(arr, x-1, y, M, N) #좌
    dfs(arr, x+1, y, M, N) #우

def bfs(arr, x, y, M, N) :
    queue = []
    queue.append([y,x])
    while len(queue) != 0 :
        y, x = queue.pop(0)
        if x < 0 or x >= M or y < 0 or y >= N :
            continue
        elif arr[y][x] == 0 :
            continue
        queue.append([y+1, x])
        queue.append([y-1, x])
        queue.append([y, x-1])
        queue.append([y, x+1])
        arr[y][x] = 0

testcase = int(sys.stdin.readline().rstrip())
for _ in range(testcase) :
    M, N, K = map(int, sys.stdin.readline().split())
    warm = 0
    arr = [[0 for i in range(M)] for i in range(N)]
    for i in range(K) : #배추심기
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1
    
    for i in range(N) :
        for j in range(M) :
            if arr[i][j] == 1 :
                warm += 1
                bfs(arr, j, i, M, N)
    print(warm)
    arr.clear()