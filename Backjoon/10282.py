import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize


def dijkstra(distance,graph,start):
    q = []
    distance[start] = 0
    heapq.heappush(q,[0,start])
    while q:
        dis,cur = heapq.heappop(q)
        if dis > distance[cur]:
            continue
        for w,node in graph[cur]:
            nw = w + dis
            if nw < distance[node]:
                distance[node] = nw
                heapq.heappush(q,[nw,node])

t = int(input())
for _ in range(t):
    n,d,c = map(int,input().split())
    distance = [inf]*(n+1)
    graph = [[] for i in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((s,a))
    dijkstra(distance,graph,c)
    cnt = 0
    sec = 0
    for d in distance:
        if d < inf:
            cnt += 1
            sec = max(sec,d)
    print("{0} {1}".format(cnt,sec))