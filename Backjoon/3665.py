from sys import stdin
from collections import deque

input = stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    size = len(arr)
    graph = [[] for i in range(n+1)]
    indegree = [0]*(n+1)
    res = []
    check = False
    question = False
    q = deque()
    for i in range(size):
        for j in range(i+1,size):
            graph[arr[i]].append(arr[j])
            indegree[arr[j]] += 1

    m = int(input())

    for _ in range(m):
        a,b = map(int,input().split())
        if a in graph[b]:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
        elif b in graph[a]:
            graph[a].remove(b)
            graph[b].append(a)
            indegree[b] -= 1
            indegree[a] += 1
    for i in range(1,len(indegree)):
        if indegree[i] == 0:
            q.append(i)
    if not q:
        check = True
    if len(q) > 1:
        question = True
    while q:
        cur = q.popleft()
        res.append(cur)
        for i in graph[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    if check or len(res) < n:
        print("IMPOSSIBLE")
    elif question:
        print("?")
    else:
        print(" ".join(list(map(str,res))))





