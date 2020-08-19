import sys

n = int(sys.stdin.readline())
for i in range(n):
    tmp = 0
    ans = 0
    for i,v in enumerate(list(map(str,sys.stdin.readline()))):
        if 'O' == v:
            tmp += 1
            ans += tmp
        else:
            tmp = 0
            ans += 0
    print(ans)


