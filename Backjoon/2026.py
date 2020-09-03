import sys, copy
from collections import deque
def check(x,y,n,m):
    return ( x>= 0 and x < n) and ( y >= 0 and y < m)
arrow = [(1,0),(0,1),(-1,0),(0,-1)]
arr = []
ans = []
breaker = 1
active = False
n,m = map(int,sys.stdin.readline().split())
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip('\n'))))

for i,col in enumerate(arr):
    for j,row in enumerate(col):
        if arr[i][j] == 1 and breaker == 1:
            arr[i][j] = 0
            breaker -=1
            active = True
        tmp = copy.deepcopy(arr)
        index = 0
        q = deque()
        q.append((0,0))
        while q:
            x,y = q.popleft()
            for d in arrow:
                nx = x + d[0]
                ny = y + d[1]
                if check(nx,ny,n,m) and tmp[nx][ny] == 0:
                    tmp[nx][ny] = tmp[x][y] + 1
                    index = tmp[nx][ny]
                    q.append((nx,ny))
        if tmp[n-1][m-1] != 0:
            ans.append(index)
        if active:
            breaker = 1
            arr[i][j] = 1
            active = False
        
if len(ans) == 0:
    index = -1
else:
    index = min(ans) +1
print(index)