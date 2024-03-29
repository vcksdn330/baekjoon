m, n = map(int, input().split())
count = 0
ans = 0
while not (m == 1 or n == 1) :
    if count == 0 :
        m -= 1
        count = 1
    else :     
        n -= 1
        count = 0
    ans += 1
print(ans + 1)
