import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize

n,m = map(int,input().split())
distance = [[inf,0,0] for i in range(n+1)]
graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
def dijkstra():
    global graph,distance,nodes
    q = []
    distance[1][0] = 0
    heapq.heappush(q,[0,1])
    while q:
        dis,cur = heapq.heappop(q)
        if dis > distance[cur][0]:
            continue
        for w,node in graph[cur]:
            nw = dis + w
            if nw < distance[node][0]:
                distance[node] = [nw,node,cur]
                heapq.heappush(q,[nw,node])

dijkstra()
cnt = 0
res = []
for i,d in enumerate(distance):
    if i != 1 and d[0] <inf:
        cnt += 1
        res.append((d[1],d[2]))
print(cnt)
for d in res:
    print("{0} {1}".format(d[0],d[1]))
