from sys import stdin

input = stdin.readline

n = int(input())
arr= []
res = 0
cnt = 0
arr = list(map(int,input().split()))
arr.sort()
for i in arr:
    cnt += 1
    if i <= cnt:
        res += 1
        cnt = 0
print(res)

