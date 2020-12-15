from sys import stdin
from collections import deque

input = stdin.readline

n,m = map(int,input().split())
direct = [(1,0),(0,1),(-1,0),(0,-1)]
visit = [[False]*m for i in range(n)]
arr = []
for i in range(n):
    arr.append(list(map(int,input().rstrip('\n'))))

def bfs(start):
    global arr,direct,visit,m,n
    q = deque()
    q.append(start)
    while q:
        y,x = q.popleft()
        for tmpY,tmpX in direct:
            nx = x + tmpX
            ny = y + tmpY
            if 0<=nx<m and 0<=ny<n and not visit[ny][nx] and arr[ny][nx] == 0:
                visit[ny][nx] = True
                q.append((ny,nx))
count = 0
for i in range(n):
    for j in range(m):
        if not visit[i][j] and arr[i][j] == 0:
            bfs((i,j))
            count += 1
print(count)