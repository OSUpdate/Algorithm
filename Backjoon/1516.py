from sys import stdin
from collections import deque
import copy
input = stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
indegree = [0]*(n+1)
times = [0]*(n+1)
for i in range(1,n+1):
    tmp = list(map(int, input().split()))
    times[i] = tmp[0]
    for j in tmp[1:-1]:
        graph[j].append(i)
        indegree[i] += 1
def topology():
    global graph,indegree,times,n
    q = deque()
    res = copy.deepcopy(times)
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            indegree[i] -= 1
            res[i] = max(res[i],res[cur]+times[i])
            if indegree[i] == 0:
                q.append(i)
    return res

res = topology()
for i in range(1,n+1):
    print(res[i])