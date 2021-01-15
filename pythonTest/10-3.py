from sys import stdin

input = stdin.readline

n, m = map(int,input().split())
edges = []
parent = [i for i in range(n+1)]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

for _ in range(m):
    a, b, c = map(int,input().split())    
    edges.append((c,a,b))
edges.sort(key=lambda x: x[0])
result = 0
last = 0
for edge in edges:
    c,a,b = edge
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        result += c
        last = c
print(result-last)
