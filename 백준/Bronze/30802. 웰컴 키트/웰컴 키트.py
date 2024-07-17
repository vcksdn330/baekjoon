n = int(input())
shirt = list(map(int, input().split()))
t, p = map(int, input().split())

ans1 = 0

for i in shirt :
    ans1 += i // t
    if i%t > 0 :
        ans1 += 1
print(ans1)
print(n//p, n%p)