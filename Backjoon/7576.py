import sys,copy
from collections import deque
def check(x,y,n,m):
    return (x>=0 and x < m) and ( y>=0 and y<n)
arrow = [(1,0),(0,1),(-1,0),(0,-1)]
n,m = map(int,sys.stdin.readline().split())
arr = []
index = 0 
q = deque()
for i in range(m):
    row = list(map(int,sys.stdin.readline().split()))
    arr.append(row)
    for j,v in enumerate(row):
        if arr[i][j] == 1:
            q.append((i,j))
while(q):
    x,y = q.popleft()
    for d in arrow:
        nx = x+d[0]
        ny = y+d[1]
        if check(nx,ny,n,m) and arr[nx][ny] == 0:
            arr[nx][ny] = arr[x][y] + 1
            index = max(arr[nx][ny],index)
            q.append((nx,ny))
if index != 0:
    index -= 1
for i in arr:
    for j in i:
        if j == 0:
            index = -1
            break
print(index)
