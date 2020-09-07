import sys
from collections import deque

knight = [(2,1),(1,2),(2,-1),(1,-2),(-2,-1),(-1,-2),(-2,1),(-1,2)]
Tcase = int(sys.stdin.readline())
for i in range(Tcase):
    n = int(sys.stdin.readline())
    arr = [[0 for i in range(n)] for j in range(n)]
    visit = [[False for i in range(n)] for j in range(n)]
    start = tuple(map(int,sys.stdin.readline().split()))
    move = tuple(map(int,sys.stdin.readline().split()))
    q = deque()
    q.append(start)
    cnt = 0
    while q:
        x,y = q.popleft()
        visit[x][y] = True
        if (x,y) == move:
            break
        for dir in knight:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                visit[nx][ny] = True
                q.append((nx,ny))
                arr[nx][ny] = arr[x][y] + 1

    print(arr[move[0]][move[1]])