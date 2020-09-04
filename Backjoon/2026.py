import sys
import copy
from collections import deque

def check(x, y, n, m):
    return (x >= 0 and x < n) and (y >= 0 and y < m)
arrow = [(1, 0), (-1, 0), (0, 1), (0, -1)]
arr = []
ans = []
temp = []
n, m = map(int, sys.stdin.readline().split())
for i in range(n):
    temp.append(list(map(int, sys.stdin.readline().rstrip('\n'))))
arr.append(temp)
arr.append(temp)
visit = []
index = 0
q = deque()
q.append((0, 0, 0, 0))
while q:
    tmp = q.popleft()
    x,y,wall,cnt = tmp
    if x == n-1 and y == m-1:
        index = cnt
        break
    for d in arrow:
        nx = x + d[0]
        ny = y + d[1]
        if check(nx, ny, n, m):
            if arr[0][nx][ny] == 1 and wall == 0:
                arr[wall+1][nx][ny] = 1
                q.append((nx, ny, 1, cnt + 1))
                visit.append((nx,ny))
            elif arr[0][nx][ny] == 0 and wall == 1 and (x,y) not in visit:
                arr[wall][nx][ny] = 1
                q.append((nx, ny, wall, cnt + 1))
                visit.append((nx,ny))
print(index)
arr[0][0][0] = 20
arr[0][0][1] = 10
print(arr)
