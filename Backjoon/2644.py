from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
v1,v2 = map(int,input().split())
m = int(input())
answer = [[] for i in range(n)]
visit = [False]*n
res = 0
for i in range(m):
    x,y = map(int,input().split())
    answer[x-1].append(y-1)
    answer[y-1].append(x-1)
def dfs(cur,value,end):
    global answer,visit,n,res
    if cur == end:
        res = value
    else:
        for nxt in answer[cur]:
            if not visit[nxt]:
                visit[nxt] = True
                dfs(nxt,value+1,end)
                visit[nxt] = False
def bfs(start,end):
    global answer,visit,n,res
    q = deque()
    q.append((start,0))
    while q:
        cur, w = q.popleft()
        if cur == end:
            return w
        for nxt in answer[cur]:
            if not visit[nxt]:
                visit[nxt] = True
                q.append((nxt,w+1))
print(answer)
visit[v2-1] = True
dfs(v2-1,0,v1-1)
print(bfs(v2-1,v1-1))
print(res if res != 0 else -1)