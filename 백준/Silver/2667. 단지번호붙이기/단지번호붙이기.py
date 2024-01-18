n = int(input())

def bfs(arr, y, x, n) :
    que = [[y, x]]
    ans = 0
    while que :
        y,x = que.pop(0)
        if 0 <= x < n and 0 <= y < n :
            if arr[y][x] == 1 :
                arr[y][x] = 0
                que.append([y,x+1])
                que.append([y,x-1])
                que.append([y+1,x])
                que.append([y-1,x])
                ans += 1
    return ans
        

arr = [[] for i in range(n)]
for i in range(n) :
    arr[i] = list(map(int, str(input())))

ans = []

for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 1 :
            ans.append(bfs(arr, i, j, n))

ans.sort()
print(len(ans))
for i in ans :
    print(i)