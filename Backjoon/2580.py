from sys import stdin

input = stdin.readline

arr = []
zero = []
for i in range(9):
    tmp = list(map(int,input().split()))
    for j,v in enumerate(tmp):
        if v == 0:
            zero.append((i,j))

    arr.append(tmp)
visit = [False] * len(zero)
check = False
def dfs(cur,end):
    global check,arr,zero,visit
    
    if check:
        return
    
    if cur == end:
        check = True
        for r in arr:
            print(*r)
        return
    else:
        i,j = zero[cur]
        ansList = [1,2,3,4,5,6,7,8,9]
        #row = arr[i]
        #col = [t[j] for t in arr]
        y,x = i//3,j//3
        #sec = [row[x*3:(x+1)*3] for row in arr[y*3:(y+1)*3]]
        visit[cur] = True
        for k in range(9):
            if arr[i][k] in ansList:
                ansList.remove(arr[i][k]) 
            if arr[k][j] in ansList:
                ansList.remove(arr[k][j])
        for r in range(y*3,(y+1)*3):
            for c in range(x*3,(x+1)*3):
                if arr[r][c] in ansList:
                    ansList.remove(arr[r][c])    
        for k in ansList:
            arr[i][j] = k
            dfs(cur+1,end)
            arr[i][j] = 0
            visit[cur] = False
end = len(zero)
dfs(0,end)