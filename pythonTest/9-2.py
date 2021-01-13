import sys,heapq

input = sys.stdin.readline
inf = sys.maxsize
n,m = map(int,input().split())
arr = [ [] for i in range(n)]
dp1 = [inf] * n
dp2 = [inf] * n
for _ in range(m):
    a,b = map(int,input().split())
    arr[a-1].append((b-1,1))
    arr[b-1].append((a-1,1))
x,k = map(int,input().split())

def dijkstra(start,dp):
    global arr
    q = []
    dp[start] = 0
    heapq.heappush(q,[start,0])
    while q:
        cur, dis = heapq.heappop(q)
        if dp[cur] < dis:
            continue
        for node,w in arr[cur]:
            nxt = dis + w
            if nxt < dp[node]:
                dp[node] = nxt
                heapq.heappush(q,[node,nxt])
print(arr)
dijkstra(0,dp1)
dijkstra(k-1,dp2)
answer = dp1[k-1] + dp2[x-1]
print(-1 if answer >= inf else answer)