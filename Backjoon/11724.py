import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
arr = [[] for i in range(n)]
visit = [False] * n
cnt = 0
for i in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    arr[v1 - 1].append(v2 - 1)
    arr[v2 - 1].append(v1 - 1)
for idx,vis in enumerate(visit):
    if not vis:
        q = deque()
        q.append(idx)
        while q:
            cur = q.pop()
            for d in arr[cur]:
                if not visit[d]: 
                    q.append(d)
                    visit[d] = True
        cnt += 1
     
print(cnt)