import sys
from collections import deque

direct = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
def check(x,y,w,h):
    return (x >= 0 and x < h) and ( y >= 0 and y < w)
def bfs(arr, w, h, x, y):
    global direct, visit
    
    q = deque()
    q.append((x,y))
    cnt = 0
    while q:
        x,y = q.popleft()
        visit[x][y] = True
        for dir in direct:
            nx = x + dir[0]
            ny = y + dir[1]
            if check(nx,ny,w,h) and arr[nx][ny] == 1 and not visit[nx][ny]:
                q.append((nx,ny))
                visit[nx][ny] = True
    return cnt
w, h = map(int,sys.stdin.readline().split())

while w != 0 and h != 0:
    arr = []
    for i in range(h):
        arr.append(list(map(int,sys.stdin.readline().split())))
    visit = [[False for i in range(w)] for j in range(h)]
    ans = []
    for x in range(h):
        for y in range(w):
            if not visit[x][y] and arr[x][y] == 1:
                ans.append(bfs(arr, w, h, x, y))
    print(len(ans))
    w, h = map(int,sys.stdin.readline().split())