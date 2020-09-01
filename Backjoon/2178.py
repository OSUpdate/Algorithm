import sys
from collections import deque

def check(x,y,n,m):
    return (x >= 0 and x <n) and (y>=0 and y < m)

def bfs(v):
    arr = [(1,0),(-1,0),(0,1),(0,-1)]
    global graph,n,m
    cnt = [[-1 for i in range(m)] for j in range(n)]
    cnt[v[0]][v[1]] = 1
    q = deque()
    q.append(v)
    while q:
        x,y = q.popleft()

        for i in arr:
            nx = i[0]+x
            ny = i[1]+y
            if check(nx,ny,n,m) and graph[nx][ny] == 1 and cnt[nx][ny] == -1:
                cnt[nx][ny] = cnt[x][y] + 1
                q.append((nx,ny))
    print(cnt[n-1][m-1])



n,m = map(int,sys.stdin.readline().split())
graph =[]
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip('\n'))))
bfs((0,0))
