import sys

n = int(input())
m = int(input())
sentence = sys.stdin.readline().rstrip()
nword = "I" + "OI" * n  
p = 0
ans = 0

while p+(2*n)+1 <= m :
    pu = 0
    if sentence[p] == "I" :
        if sentence[p:p+(n*2+1)] == nword :
            ans += 1
            pu += n*2+1
            tmp = 1
            while p+(n*2)+1+(tmp*2) <= m :
                if sentence[p+n*2+tmp*2-1 : p+n*2+tmp*2+1] == "OI" :
                    ans += 1
                    pu += 2
                    tmp += 1
                else :
                    break
            p += pu
        else :
            p+= 1
    else :
        p += 1

print(ans)