import sys
from collections import deque
def check(x,y,n):
    return (x>=0 and x <n) and (y>=0 and y < n)
n = int(sys.stdin.readline())
ans = []
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip('\n'))))
arrow = [(0,1),(1,0),(0,-1),(-1,0)]
visit = []
for l1,item in enumerate(arr):
    for l2,row in enumerate(item):
        if row == 1:
            q = deque()
            index = 1
            q.append((l1,l2))
            while q:
                x,y = q.popleft()
                visit.append((x,y))
                for i in arrow:
                    tmp_x,tmp_y = i
                    nx = x+tmp_x
                    ny = y+tmp_y
                    if check(nx,ny,n) and arr[nx][ny] == 1 and  (nx,ny) not in visit:
                        q.append((nx,ny))
                        arr[nx][ny] = 0
                        visit.append((nx,ny))
                        index += 1
            ans.append(index)
ans.sort()
print(len(ans))
for i in ans:
    print(i)

