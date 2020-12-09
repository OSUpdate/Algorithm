from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())
mst = []
p = [i for i in range(n)]
rank = [0 for i in range(n)]
for _ in range(m):
    u, v, w = map(int,input().split())
    mst.append((u,v,w))
mst.sort(key=lambda x: x[2])

def find(p,num):
    if p[num] == num:
        return num
    p[num] = find(p,p[num])
    return p[num]

def union(p,a,b):
    global rank
    if rank[a] > rank[b]:
        p[b] = a
    else:
        p[a] = b
        if rank[a] == rank[b]:
            rank[b] += 1

def kruskal():
    global mst,p,m
    minimum = 0
    for i in range(m):
        u,v,w = mst[i]
        v1 = find(p,u-1)
        v2 = find(p,v-1)
        if v1 != v2:
            union(p,v1,v2)
            minimum += w
    return minimum

print(kruskal())