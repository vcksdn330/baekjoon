n, value = map(int, input().split())
arr = []
for i in range(n) :
    arr.append(int(input()))
ans = 0
for i in range(1,n+1) : #뒤에서부터 봄(내림차순)
    while arr[-i] <= value :
        value -= arr[-i]
        ans += 1
    if value == 0 :
        break
print(ans)