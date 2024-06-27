import sys

t = int(input())

def fac(x) :
    ans = 1
    for i in range(2,x+1) :
        ans *= i
    return ans

for _ in range(t) :
    n, m = map(int, input().split())
    print((fac(m)//fac(m-n))//fac(n))
