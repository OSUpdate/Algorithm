from sys import stdin
from collections import deque

input = stdin.readline

n,m = map(int,input().split())

direct = [(1,0),(-1,0),(0,1),(0,-1)]

arr = []

for _ in range(n):
    arr.append(list(map(int,input().rstrip('\n'))))

def bfs(start):
    global direct,arr
    q = deque()
    q.append(start)
    while q:
        y,x = q.popleft()
        for tmpY,tmpX in direct:
            nx = x + tmpX
            ny = y + tmpY
            if 0<=nx<m and 0<=ny<n and arr[ny][nx] == 1:
                arr[ny][nx] = arr[y][x] + 1
                q.append((ny,nx))
bfs((0,0))
print(arr[n-1][m-1])