import sys

input = sys.stdin.readline

inf = sys.maxsize
n = int(input())
m = int(input())
graph = [[0 if i==j else inf for j in range(n)] for i in range(n)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = min(c,graph[a-1][b-1])
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
for i in graph:
   for j in i:
        if j == inf:
            print(0, end='')
        else:
            print(j, end='')
    print()