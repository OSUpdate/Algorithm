import sys
import copy 
n,m = map(int,sys.stdin.readline().split())
arr = []
loc = []
ans = 0
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
k = int(sys.stdin.readline())

for i in range(k):
    loc.append(list(map(int,sys.stdin.readline().split())))
tmp = copy.deepcopy(arr)
for i,v in enumerate(arr):
    for j in range(m-1):
        arr[i][j+1] += arr[i][j]
for i in range(m):
    for j in range(n-1):
        arr[j+1][i] += arr[j][i]
for i in loc:
    if i[0] == i[2] and i[1] == i[3]:
        ans = tmp[i[0]-1][i[1]-1]
        print(ans)
        continue
    if i[0] == 1 and i[1] == 1:
        ans = arr[i[2]-1][i[3]-1]
        print(ans)
        continue
    if i[0] != 1 and i[1] == 1:
        ans = arr[i[2]-1][i[3]-1] - arr[i[0]-2][i[3]-1]
        print(ans)
        continue
    if i[0] == 1 and i[1] != 1:
        ans = arr[i[2]-1][i[3]-1] - arr[i[2]-1][i[1]-2]
        print(ans)
        continue
    if i[0] != 1 and i[1] != 1:
        ans = arr[i[2]-1][i[3]-1] - arr[i[2]-1][i[1]-2] - arr[i[0]-2][i[3]-1] + arr[i[0]-2][i[1]-2]
        print(ans)
        continue
