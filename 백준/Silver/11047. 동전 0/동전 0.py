n, value = map(int, input().split())
arr = []
for i in range(n) :
    arr.append(int(input()))
ans = 0
for i in range(1,n+1) : #뒤에서부터 봄(내림차순)
    if arr[-i] <= value :
        ans += value // arr[-i]
        value = value % arr[-i]
    if value == 0 :
        break
print(ans)