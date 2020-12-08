from sys import stdin

input = stdin.readline

v, e = map(int,input().split())
mst = []

for i in range(e):
    a,b,c = map(int,input().split())
    mst.append((c,a,b))
mst.sort(key=lambda x: x[0])
parent = [i for i in range(0,v)]
rank = [0 for i in range(0,v)]
def getParent(parent,num):
    if parent[num] == num:
        return num
    parent[num] = getParent(parent,parent[num])
    return parent[num]
def union(parent,a,b):
    global rank
    if rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        if rank[b] == rank[a]:
            rank[b] += 1
def Kmst():
    global mst,e,parent
    minimum = 0
    
    for i in range(e):
        w,u,v = mst[i]
        v1 = getParent(parent,u-1)
        v2 = getParent(parent,v-1)
        if v1 != v2:
            union(parent,v1,v2)
            minimum += w
    return minimum
print(Kmst())

