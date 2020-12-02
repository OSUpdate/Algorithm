from sys import stdin
from collections import deque

input = stdin.readline

m,n,k = map(int,input().split())
arr =[[0]*n for _ in range(m)]
visit = [[False] *n for _ in range(m)]
direct = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(y,x):
    global arr,visit,direct,m,n
    cnt = 0
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        visit[y][x] = True
        cnt += 1
        for dir in direct:
            nx = x + dir[1]
            ny = y + dir[0]
            if 0<=nx<n and 0<=ny<m and not visit[ny][nx] and arr[ny][nx] ==0:
                
                q.append((nx,ny))
                visit[ny][nx] = True
    return cnt

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] += 1
answer = []
for i in range(m):
    for j in range(n):
        if not visit[i][j] and arr[i][j] == 0:
            answer.append(bfs(i,j))
answer.sort()
print(len(answer))
print(' '.join(map(str,answer)))