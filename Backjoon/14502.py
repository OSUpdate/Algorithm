import sys, copy
from _collections import deque
def IsInside(x,y,n,m):
    return (x>=0 and x<n) and (y >= 0 and y<m)
def wall(cnt,startW):
    global arr,n,m,starts,direct,ans,wallMap
    if cnt == 3:
        q = deque()
        visit = []
        temp = copy.deepcopy(wallMap)
        for start in starts:
            q.append(start)
            while len(q) != 0:
                x,y = q.popleft()
                visit.append((x,y))
                for dir in direct:
                    next_x,next_y = dir
                    next_x += x
                    next_y += y
                    if IsInside(next_x,next_y,n,m) and temp[next_x][next_y] == 0 and (next_x,next_y) not in visit:
                        temp[next_x][next_y] = 2
                        q.append((next_x,next_y))
                        visit.append((next_x,next_y))
        zero = 0
        for v in temp:
            zero += v.count(0)
        if zero == 6:
            for e in temp:
                print(e)
            print(starts)
        ans=max(ans,zero)
        return
    else:
        for i in range(startW, n*m):
            r = i // m
            c = i % m
            if wallMap[r][c] == 0:
                wallMap[r][c] = 1
                wall(cnt+1,i)
                wallMap[r][c] = 0
            

starts = []
direct = [(1,0),(-1,0),(0,1),(0,-1)]
ans = 0
n, m = map(int, sys.stdin.readline().split())
arr = []
wallMap = []
cnt = 0
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    arr.append(tmp)
for i,v1 in enumerate(arr):
    for j,v2 in enumerate(v1):
        if v2 == 2:
            starts.append((i,j))


for i in range(n*m):
    r = i // m
    c = i % m
    if arr[r][c] == 0:
        wallMap = copy.deepcopy(arr)
        wallMap[r][c] = 1
        wall(1,i)
        wallMap[r][c] = 0
print(ans)
