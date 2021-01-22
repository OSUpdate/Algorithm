import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize
direct = [(1,0),(0,1),(-1,0),(0,-1)]


n = int(input())
arr = []
distance = [[inf]*n for i in range(n)]
for _ in range(n):
    arr.append(list(map(int,input().rstrip("\n"))))
def dijkstra():
    global distance,direct,arr
    q = []
    heapq.heappush(q,[0,0,0])
    distance[0][0] = 0
    while q:
        w,y,x = heapq.heappop(q)
        for dir in direct:
            ny = y + dir[0]
            nx = x + dir[1]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[ny][nx] == 0:
                    nw = w + 1
                    if distance[ny][nx] > nw:
                        distance[ny][nx] = nw
                        heapq.heappush(q,[nw,ny,nx]) 
                else:
                    if distance[ny][nx] > distance[y][x]:
                        distance[ny][nx] = distance[y][x]
                        heapq.heappush(q,[w,ny,nx]) 
dijkstra()
print(distance[n-1][n-1])
