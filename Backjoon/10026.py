import sys
from collections import deque

def bfs(i,j,n,check):
    global arr,visit,dir
    cur = arr[i][j]
    q = deque()
    q.append((i,j))
    while q:
        x,y = q.popleft()
        visit[x][y] = True
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if check and (cur == 'G' or cur =='R'):
                if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and (arr[nx][ny] == 'G' or arr[nx][ny] == 'R'):
                    visit[nx][ny] = True
                    q.append((nx,ny))
            else:
                if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and cur == arr[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx,ny))
    return 1

dir = [(1,0),(-1,0),(0,1),(0,-1)]
n = int(sys.stdin.readline())
arr = []
cnt = 0
visit = [[False for i in range(n)] for j in range(n)]
for i in range(n):
    arr.append(list(map(str,sys.stdin.readline().rstrip('\n'))))
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            cnt += bfs(i,j,n,False)
ans = [str(cnt)]
cnt = 0
visit = [[False for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            cnt += bfs(i,j,n,True)
ans.append(str(cnt))
print(" ".join(ans))