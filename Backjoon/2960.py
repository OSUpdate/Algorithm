import sys

n,k = map(int,sys.stdin.readline().split())

nList = []
ans = []
for i in range(2,n+1):
    nList.append(i)
for i in range(2,n+1):
    for j,v in enumerate(nList):
        if v%i ==0:
            del nList[j]
            ans.append(v)
print(ans[k-1])
