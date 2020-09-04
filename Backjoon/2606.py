import sys
from collections import deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [[] for i in range(n)]
cnt = 0
visit = []
for i in range(m):
    v1,v2 = map(int,sys.stdin.readline().split())
    arr[v1-1].append(v2-1)
    arr[v2-1].append(v1-1)
for data in arr:
    data.sort()
q = deque()
q.append(0)
while q:
    x = q.popleft()
    visit.append(x)
    for _,d in enumerate(arr[x]):
        if d not in visit:
            q.append(d)
            visit.append(d)
            cnt += 1
print(cnt)
