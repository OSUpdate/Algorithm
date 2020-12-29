from sys import stdin

input = stdin.readline

dir = [(0,1),(1,0),(0,-1),(-1,0)]
cur = 0
change = []
sec = 0
size = 0
snake = [(0,0)]

n = int(input())
k = int(input())

arr = [[0]*n for i in range(n)]
arr[0][0] = 2
for i in range(k):
    r,c = map(int,input().split())
    arr[r-1][c-1] = 1

L = int(input())
for i in range(L):
    x,c = input().rstrip('\n').split()
    change.append((int(x),c))

while True:
    fy,fx = snake[0]

    t,l = change[size]
    if sec == t: 
        if l == 'D':
            cur += 1
            if cur > 3:
                cur = 0
        else:
            cur -= 1
            if cur < 0:
                cur = 3
        if size < L-1:
            size += 1
    cury,curx = dir[cur]
    ny,nx  = fy+cury, fx+curx
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        sec+=1
        break
    if arr[ny][nx] == 2:
        sec+=1
        break
    if arr[ny][nx] == 1:
        snake.append(snake[-1])
    ly,lx = snake[-1]
    arr[ly][lx] = 0
    for d in range(len(snake)-1,0,-1):
        snake[d] = snake[d-1]
    snake[0] = (ny,nx)
    arr[ny][nx] = 2
    sec += 1
    for d in arr:
        print(d)
    print(sec)
print(sec)

    