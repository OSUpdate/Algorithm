from sys import stdin
from collections import deque

input = stdin.readline

direct = [(1,0),(0,1),(-1,0),(0,-1)]
n = int(input())
arr = []
maximum = 0

def bfs(y,x):
    global arr,direct,n,visit
    q = deque()
    cnt = 0
    q.append((x,y))
    while q:
        x,y = q.popleft()
        visit[y][x] = True
        for dir in direct:
            nx = x + dir[1]
            ny = y + dir[0]
            if 0<=nx<n and 0<=ny<n and arr[ny][nx] != 0 and not visit[ny][nx]:
                cnt += 1
                q.append((nx,ny))
                visit[ny][nx] = True
    return cnt
for i in range(n):
    arr.append(list(map(int,input().split())))
    maximum = max(max(arr[i]),maximum)
answer = []

for h in range(0,maximum+1):
    tmp = []
    visit = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= h:
                arr[i][j] = 0
    for y in range(n):
        for x in range(n):
            if not visit[y][x] and arr[y][x] !=0:
                tmp.append(bfs(y,x))
    answer.append(len(tmp))
print(max(answer))