from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visit = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dir = [(1,0),(0,1),(-1,0),(0,-1)]
q = deque()
tmprx, tmpry, tmpbx, tmpby = [0]*4
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            tmprx, tmpry = i, j
        elif arr[i][j] == 'B':
            tmpbx, tmpby = i, j
q.append((tmprx, tmpry, tmpbx, tmpby, 1))
visit[tmprx][tmpry][tmpbx][tmpby] = True
    

def move(x, y, tdx, tdy):
    c = 0
    while arr[x+tdx][y+tdy] != '#' and arr[x][y] != 'O':
        x += tdx
        y += tdy
        c += 1
    return x, y, c

def bfs():
    while q:
        rx, ry, bx, by, ans = q.popleft()
        if ans > 10:
            break
        for i,d in enumerate(dir):
            nrx, nry, rc = move(rx, ry, d[0], d[1])
            nbx, nby, bc = move(bx, by, d[0], d[1])
            if arr[nbx][nby] == 'O':
                continue
            if arr[nrx][nry] == 'O':
                print(1)
                return
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= d[0]
                    nry -= d[1]
                else:
                    nbx -= d[0]
                    nby -= d[1]
            if not visit[nrx][nry][nbx][nby]:
                visit[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, ans+1))
    print(0)

bfs()

