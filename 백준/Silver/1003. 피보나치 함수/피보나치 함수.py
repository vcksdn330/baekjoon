import sys

fib = [0, 1]

def fibbo(n):
    if len(fib) > n:
        return fib[n]
    else:
        fib.append(fibbo(n-1) + fibbo(n-2))
        return fibbo(n-1) + fibbo(n-2)

fibbo(40)

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    m = int(sys.stdin.readline().rstrip())
    if m == 0:
        print(1, 0)
    else:
        print(fib[m-1], fib[m])