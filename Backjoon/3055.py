from collections import deque
from sys import stdin

input = stdin.readline
direct = [(1,0),(0,1),(-1,0),(0,-1)]
r,c = map(int,input().split())
arr = []
start = []
water = []
endy,endx = 0,0
visit = [[0]*c for i in range(r)]
for i in range(r):
    tmp = list(map(str,input().rstrip('\n')))
    for j in range(c):
        if tmp[j] == '*':
            water.append((i,j))
        elif tmp[j] == 'S':
            start.append((i,j))
        elif tmp[j] == 'D':
            endy,endx =i,j

    arr.append(tmp)
print(arr[18][21])
def bfs(start,water):
    global direct,r,c,arr
    q = deque()
    for v in water:
        q.append(v)
    q.append(start[0])
    while q:
        y,x = q.popleft()
        for dir in direct:
            ny = y + dir[0]
            nx = x + dir[1]
            if 0<= ny < r and 0<=nx<c:
                if arr[y][x] == '*':
                    if arr[ny][nx] == '.':
                        arr[ny][nx] = '*'
                        q.append((ny,nx))
                elif arr[y][x] == 'S':
                    
                    if arr[ny][nx] == '.':
                        visit[ny][nx] = visit[y][x] + 1
                        arr[ny][nx] = 'S'
                        q.append((ny,nx))
                    elif arr[ny][nx] == 'D':
                        visit[ny][nx] = visit[y][x] + 1
                        return

bfs(start,water)
print('KAKTUS' if visit[endy][endx] == 0 else visit[endy][endx])

#for i in visit:
#    print(i)
