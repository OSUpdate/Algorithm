import sys,heapq

input = sys.stdin.readline
inf = sys.maxsize

n,m,c = map(int, input().split())
graph = [[] for i in range(n)]
dp = [inf]*n
for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x-1].append((y-1,z))

def dijkstar(start):
    global graph
    q = []
    heapq.heappush(q,[start,0])
    while q:
        cur, dis = heapq.heappop(q)
        if dp[cur] < dis:
            continue
        for node,w in graph[cur]:
            nxt = dis + w
            if nxt < dp[node]:
                dp[node] = nxt
                heapq.heappush(q,[node,nxt])
dijkstar(c-1)
cnt = 0
maximum = 0
for i in dp:
    if i < inf:
        cnt += 1
        maximum = max(i,maximum)
print(cnt,maximum)

    