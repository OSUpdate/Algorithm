from sys import stdin

input = stdin.readline

n = int(input())
arr= []
visit = [False]*n
for _ in range(n):
    arr.append(tuple(map(int,input().split())))
arr.sort(key=lambda x:(x[1],x[0]))
cnt = 1
end = arr[0][1]
for i in range(1,len(arr)):
    if arr[i][0] >= end:
        end = arr[i][1]
        cnt += 1
print(cnt)