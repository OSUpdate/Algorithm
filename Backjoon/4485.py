import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize
direct = [(1,0),(0,1),(-1,0),(0,-1)]

def dijkstra():
    global n,distance,arr,visit
    q = []
    heapq.heappush(q,[arr[0][0],0,0,])
    distance[0][0] = 0
    while q:
        w,y,x= heapq.heappop(q)

        for dir in direct:
            ny = y + dir[0]
            nx = x + dir[1]
            if 0<=ny<n and 0<=nx<n:
                nw = w+arr[ny][nx]
                if nw < distance[ny][nx]:
                    distance[ny][nx] = nw
                    heapq.heappush(q,[nw,ny,nx]) 

num = 1
while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    visit = [[False]*n for i in range(n) ] 
    distance = [[inf]*n for i in range(n)]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    dijkstra()
    print("Problem {0}: {1}".format(num,distance[n-1][n-1]))
    num += 1


