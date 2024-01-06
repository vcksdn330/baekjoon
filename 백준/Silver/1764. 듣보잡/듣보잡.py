n, m = map(int, input().split())
an = []
am = []
for _ in range(n) :
    an.append(input())
for _ in range(m) :
    am.append(input())

sn = set(an)
sm = set(am)
ans = sn & sm
sans = list(ans)
sans.sort()
print(len(ans))
for i in sans :
    print(i)