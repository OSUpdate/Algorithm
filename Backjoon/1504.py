import sys
import heapq

input = sys.stdin.readline

n,e = map(int,input().split())
arr = [{} for i in range(n)]
inf = sys.maxsize
for _ in range(e):
    a,b,c = map(int,input().split())
    arr[a-1][b-1] = c
    arr[b-1][a-1] = c
v1, v2 = map(int,input().split())
d = [inf] * n
d1 = [inf] * n
d2 = [inf] * n
visit = [False]*n
def dijstra(start,d):
    global arr,visit
    q = []
    d[start] = 0
    heapq.heappush(q,[start,0])
    while q:
        cur, dis = heapq.heappop(q)
        for node,w in arr[cur].items():
            nxt = dis+w
            if nxt < d[node]:
                visit[node] = True
                d[node] = nxt
                heapq.heappush(q,[node,nxt])
answer = 0
dijstra(0,d)
dijstra(v1-1,d1)
dijstra(v2-1,d2)

answer = min(d[v1-1]+d1[v2-1]+d2[n-1], d[v2-1]+d2[v1-1]+d1[n-1])
print(answer)
print(-1 if answer >= inf else answer)