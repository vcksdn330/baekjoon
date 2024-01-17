n = int(input())
field = [[] for i in range(n)]
for i in range(n) :
    field[i] = list(map(int, input().split()))

def paper(arr, n, a, b) :
    x = arr[a][b]
    ch = 0
    for i in range(n) :
        for j in range(n) :
            if x != arr[a+i][b+j] :
                ch = 1
                h = n // 2
                return (
                        paper(arr, h, a, b) + 
                        paper(arr, h, a+h, b) +
                        paper(arr, h, a, b+h) + 
                        paper(arr, h, a+h, b+h)
                        )
                break
    if ch == 0 :
        if x == 1 :
            return 10**4
        else :
            return 1
    return 0

ans = paper(field, n, 0, 0)
b = ans // 10000
w = ans - b*10000
print(w)
print(b)