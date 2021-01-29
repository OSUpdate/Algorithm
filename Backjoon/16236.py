from sys import stdin
from collections import deque

input = stdin.readline
direct = [(1,0),(-1,0),(0,-1),(0,1)]
n = int(input())
arr = []

start = [0,0,2,0,0]
for i in range(n):
    tmp = list(map(int,input().split()))
    if 9 in tmp:
        y,x = i,tmp.index(9)
        
    arr.append(tmp)
arr[y][x] = 0
def bfs(y,x,state,cnt):
    global arr, direct,n
    q = deque()
    q.append((y,x))
    visit = [[False]*n for _ in range(n)]
    dist = [[0]*n for _ in range(n)]
    visit[y][x] = True
    can = []
    while q:
        y,x = q.popleft()
        for d in direct:
            ny = y + d[0]
            nx = x + d[1]
            if 0 <= ny < n and 0<= nx < n and not visit[ny][nx]:
                if state >= arr[ny][nx] or arr[ny][nx] == 0:
                    visit[ny][nx] = True
                    dist[ny][nx] = dist[y][x] + 1

                    q.append((ny,nx))
                if state > arr[ny][nx] and arr[ny][nx] !=0:
                    can.append((ny,nx,dist[ny][nx]))
    print(can)
    if not can:
        return -1, -1,-1,-1,-1
    can.sort(key=lambda x:(x[2],x[0],[1]))
    cnt += 1
    if cnt == state:
        cnt = 0
        state += 1
    arr[can[0][0]][can[0][1]] = 0
    print(dist,can[0])
    return can[0][0],can[0][1],state,can[0][2],cnt
state,time,cnt  = 2,0,0
res = 0
while True:
    y,x,state,time,cnt = bfs(y,x,state,cnt)
    print(y,x,state,time,cnt)
    if y == -1:
        break
    res += time

print(res)