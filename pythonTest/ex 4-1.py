from sys import stdin
from collections import deque

input = stdin.readline

direct = {'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
n = int(input())
arr = input().rstrip('\n').split()
data = [[False] * n for i in range(n)]

answer = tuple()
def solution():
    global arr,data
    x,y = 0,0
    data[0][0] = True
    for cur in arr:
        tmpY,tmpX = direct[cur]
        nx = x+tmpX
        ny = y+tmpY
        if 0<=nx<n and 0<=ny<n and not data[ny][nx]:
            print(ny,nx)
            data[ny][nx] = True
            x = nx
            y = ny
    print(y+1,x+1)
solution()