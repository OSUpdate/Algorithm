from sys import stdin

input = stdin.readline

n = int(input())
data = []
ans = [1] *n
for i in range(n):
    w,h = map(int,input().split())
    data.append((w,h))
for i in range(n):
    for j in range(n):
        if data[i][0] > data[j][0] and data[i][1] > data[j][1]:
            ans[j] += 1
print(' '.join(map(str,ans)))
