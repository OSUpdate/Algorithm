import sys
from collections import deque
def bfs(n,m):
    visit = [False] * 100001
    q = deque()
    q.append((n,0))
    visit.append(n)
    while q:
        x,cnt = q.popleft()
        
        if x == m:
            return cnt
        for i in [x+1,x-1,x*2]:
            if i > 100000 or i < 0:
                continue
            if not visit[i]:
                visit[i] = True
                q.append((i, cnt+1))
         
n, m = map(int,sys.stdin.readline().split())

print(bfs(n,m))