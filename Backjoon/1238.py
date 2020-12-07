import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int,input().split())
inf = sys.maxsize
dp1 = [inf] * n
dp2 = [inf] * n
arr = [{} for i in range(n)]
d = [{} for i in range(n)]
answer = [0]*n
for _ in range(m):
    u,v,w = map(int,input().split())
    arr[u-1][v-1] = w
    d[v-1][u-1] = w

def dijstra(arr,dp,start):
    q = []
    dp[start] = 0
    heapq.heappush(q,[start,0])
    while q:
        cur,dis = heapq.heappop(q)
        for node,w in arr[cur].items():
            nxt = w+dis
            if dp[node] > nxt:
                dp[node] = nxt
                heapq.heappush(q,[node,nxt])
dijstra(arr,dp1,x-1)
dijstra(d,dp2,x-1)
answer = [dp1[i] + dp2[i] for i in range(n)]
print(max(answer))
