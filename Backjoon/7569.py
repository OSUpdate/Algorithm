import sys
from collections import deque

m, n, k = map(int,sys.stdin.readline().split())
arrow = [(1,0,0),(0,1,0),(-1,0,0),(0,-1,0),(0,0,1),(0,0,-1)]
#visit = [[[False for i in range(m)] for j in range(n)] for w in range(k)]
arr = []
zero = 0
zcheck = 0
q = deque()
for i in range(k):
    tmp = []
    for j in range(n):
        row = list(map(int,sys.stdin.readline().split()))
        tmp.append(row)
        for idx,v in enumerate(row):
            if tmp[j][idx] == 0:
                zero += 1
            if tmp[j][idx] == 1:
                q.append((j,idx,i))
                
    arr.append(tmp)
index = 0
while q:
    x,y,z = q.popleft()

    for d in arrow:
        nx = x+d[0]
        ny = y+d[1]
        nz = z+d[2]
        if (0 <= nx < n) and (0 <= ny < m) and (0 <= nz < k) and arr[nz][nx][ny] == 0:
            zcheck += 1
            arr[nz][nx][ny] = arr[z][x][y] + 1
            index = arr[nz][nx][ny]
            q.append((nx,ny,nz))
if index != 0:
    index -= 1
if zero != zcheck:
    index = -1
print(index)