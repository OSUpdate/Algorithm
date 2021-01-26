from sys import stdin

input = stdin.readline

n = int(input())
arr = []
for _ in range(n): 
    arr.append(tuple(map(int,input().split())))
arr.sort(key= lambda x:x[0])
lis = [1]
for i in range(1,n):
    lis.append(1)
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            lis[i] = max(lis[i],lis[j]+1)
print(n-max(lis))