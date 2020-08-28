import sys,math

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
ans = []
for i in range(m,n+1):
    if int(math.sqrt(i)) == math.sqrt(i) :
        ans.append(i)
if ans:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)