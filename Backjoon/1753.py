from sys import stdin
import heapq

input = stdin.readline
inf = 1000000000
V,E = map(int,input().split())
start = int(input())
arr = [[] for i in range(V+1)]
distance = [inf] * (V+1)

def dijkstraQ(num):
    global distance,arr
    q = []
    distance[num] = 0
    heapq.heappush(q,[0,num])
    while q:
        dis,cur = heapq.heappop(q)
        if distance[cur] < dis:
            continue
        for w,node in arr[cur]:
            nxt_dist = w+dis
            if nxt_dist < distance[node]:
                distance[node] = nxt_dist
                heapq.heappush(q,[nxt_dist,node])
for _ in range(E):
    u,v,w = map(int,input().split())
    arr[u].append((w,v))
dijkstraQ(start)
for i in range(1,V+1):
    print('INF' if distance[i] == inf else distance[i])