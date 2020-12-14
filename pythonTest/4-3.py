from sys import stdin

input = stdin.readline

n,m = map(int,input().split())
x,y,d = map(int,input().split())
direct = {0:(-1,0),1:(0,-1),2:(1,0),3:(0,1)}
visit = [[False]*m for i in range(n)]
arr = []
stop = False
for _ in range(n):
    arr.append(list(map(int,input().split())))
count = 1
visit[y][x] = True
while not stop:
    check = False
    for i in range(4):
        d += 1
        if d > 3:
            d = 0
        dirY,dirX = direct[i]
        nx = x + dirX
        ny = y + dirY
        if 0<=nx<m and 0<=ny<n and not visit[ny][nx] and arr[ny][nx] == 0:
            print(ny,nx)
            check = True
            visit[ny][nx] = True
            x = nx
            y = ny
            count += 1
    if not check:
        backY,backX = direct[d]
        x -= backX
        y -= backY
        if arr[y][x] == 1:
            stop = True
print(count)
