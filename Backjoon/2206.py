import sys, copy
from collections import deque

def bfs(n,m):
    global arr,visit,arrow
    index = -1
    q = deque()
    q.append((0,0,0))
    while q:
        x,y,wall = q.popleft()
        if x == n-1 and y == m-1:
            return visit[x][y][wall] + 1
        for d in arrow:
            nx = x + d[0]
            ny = y + d[1]
            if check(nx,ny,n,m) and visit[nx][ny][wall] == 0:
                if arr[nx][ny] == 0:
                        visit[nx][ny][wall] = visit[x][y][wall] + 1
                        q.append((nx,ny,wall))
                if arr[nx][ny] == 1 and wall == 0:
                    visit[nx][ny][1] = visit[x][y][wall] + 1
                    q.append((nx,ny,1))
    return -1
def check(x,y,n,m):
    return ( x>= 0 and x < n) and ( y >= 0 and y < m)
arrow = [(1,0),(0,1),(-1,0),(0,-1)]
arr = []

n,m = map(int,sys.stdin.readline().split())
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip('\n'))))
visit = [[[0,0] for i in range(m)] for j in range(n)]

print(bfs(n,m))