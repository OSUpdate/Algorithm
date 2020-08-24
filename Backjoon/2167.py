import sys

n,m = map(int,sys.stdin.readline().split())
arr = []
loc = []
ans = 0
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
k = int(sys.stdin.readline())

for i in range(k):
    loc.append(list(map(int,sys.stdin.readline().split())))

for c,rf in enumerate(loc):
    ans = 0
    print(rf,arr[0][1])
    for i in range(rf[0]-1,rf[2]):
        for j in range(rf[1]-1,rf[3]):
            ans += arr[i][j]
    print(ans)