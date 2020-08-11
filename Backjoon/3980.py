import sys
maxtotal = 0
def path(arr,pre,inp,vis,i):
    if i == 11:
        ans=list(map(int,pre.split()))
        global maxtotal
        total = 0
        for a,b in enumerate(ans):
            total += inp[a][b]
        if maxtotal < total:
            maxtotal = total
        return 
    for j,v in enumerate(arr[i]):
        if not vis[v]:
            vis[v] = True
            tmp = pre+str(v)+ " "
            path(arr,tmp,inp,vis,i+1)
            vis[v] = False

c = int(sys.stdin.readline())

for i in range(c):
    inp = []
    ans=[]
    player = [[] for t in range(11)]
    vis = [False]*11
    for j in range(11):
        arr = list(map(int,sys.stdin.readline().split()))
        inp.append(arr)
        player[j] = [i for i, v in enumerate(arr) if v>0]
    path(player,"",inp,vis,0)
    print(maxtotal)
    maxtotal = 0
